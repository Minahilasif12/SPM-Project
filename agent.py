"""
Market Trend Monitor Agent - Worker Implementation
Simple, lightweight implementation using basic Python and Flask

Team: Abdul Hannan (22i-2441), Agha Ahsan (22i-1117), Minahil Asif (22i-2710)
Course: Fundamentals of Software Project Management
Instructor: Dr. Behjat Zuhaira
"""

from flask import Flask, request, jsonify
from datetime import datetime
import json
import logging
import uuid
import statistics
from collections import deque

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agent.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Agent Configuration
AGENT_CONFIG = {
    "agent_id": "market-trend-agent-001",
    "agent_name": "Market Trend Monitor",
    "version": "1.0.0",
    "team": [
        {"name": "Abdul Hannan", "roll": "22i-2441", "role": "Project Manager"},
        {"name": "Agha Ahsan", "roll": "22i-1117", "role": "Data & Testing"},
        {"name": "Minahil Asif", "roll": "22i-2710", "role": "Lead Developer"}
    ],
    "capabilities": [
        "trend_analysis",
        "sentiment_analysis", 
        "price_prediction",
        "anomaly_detection"
    ]
}

# Memory Storage (Simple in-memory storage)
class SimpleMemory:
    def __init__(self):
        self.short_term = deque(maxlen=50)  # Last 50 tasks
        self.long_term = []  # Important patterns
        self.max_long_term = 1000
    
    def add_short_term(self, data):
        """Add to short-term memory"""
        data['stored_at'] = datetime.now().isoformat()
        self.short_term.append(data)
        logger.debug(f"Added to short-term memory: {data.get('task_id', 'unknown')}")
    
    def add_long_term(self, data):
        """Add to long-term memory"""
        data['stored_at'] = datetime.now().isoformat()
        self.long_term.append(data)
        
        # Keep only last N entries
        if len(self.long_term) > self.max_long_term:
            self.long_term.pop(0)
        logger.debug(f"Added to long-term memory: {data.get('task_id', 'unknown')}")
    
    def get_stats(self):
        """Get memory statistics"""
        return {
            "short_term_count": len(self.short_term),
            "long_term_count": len(self.long_term),
            "short_term_capacity": self.short_term.maxlen,
            "long_term_capacity": self.max_long_term
        }

# Initialize memory
memory = SimpleMemory()

# Analysis Functions
def analyze_trend(data):
    """
    Analyze market trend from price data
    Returns: bullish, bearish, or neutral
    """
    try:
        prices = data.get('prices', [])
        volumes = data.get('volumes', [])
        market = data.get('market', 'UNKNOWN')
        
        if len(prices) < 2:
            return {
                "status": "error",
                "message": "Need at least 2 price points"
            }
        
        # Calculate price change percentage
        price_change = ((prices[-1] - prices[0]) / prices[0]) * 100
        
        # Calculate average volume
        avg_volume = sum(volumes) / len(volumes) if volumes else 0
        
        # Determine trend
        if price_change > 2:
            trend = "bullish"
            strength = "strong" if price_change > 5 else "moderate"
        elif price_change < -2:
            trend = "bearish"
            strength = "strong" if price_change < -5 else "moderate"
        else:
            trend = "neutral"
            strength = "weak"
        
        # Generate insights
        insights = []
        if abs(price_change) > 5:
            direction = "upward" if price_change > 0 else "downward"
            insights.append(f"Strong {direction} momentum detected")
        
        if avg_volume > 1000000:
            insights.append("High trading volume indicates strong market activity")
        
        result = {
            "trend": trend,
            "strength": strength,
            "price_change_percent": round(price_change, 2),
            "current_price": prices[-1],
            "average_volume": round(avg_volume, 2),
            "insights": insights
        }
        
        logger.info(f"Trend analysis for {market}: {trend} ({strength})")
        return result
        
    except Exception as e:
        logger.error(f"Trend analysis error: {str(e)}")
        return {"status": "error", "message": str(e)}


def analyze_sentiment(data):
    """
    Analyze sentiment from text data using keyword matching
    Returns: positive, negative, or neutral
    """
    try:
        texts = data.get('texts', [])
        market = data.get('market', 'UNKNOWN')
        
        if not texts:
            return {
                "status": "error",
                "message": "No text data provided"
            }
        
        # Sentiment keywords
        positive_words = ['bullish', 'growth', 'profit', 'surge', 'rally', 'gain', 
                         'rise', 'boost', 'strong', 'positive', 'up', 'high']
        negative_words = ['bearish', 'loss', 'decline', 'crash', 'drop', 'fall',
                         'down', 'weak', 'negative', 'risk', 'low', 'bear']
        
        positive_count = 0
        negative_count = 0
        
        # Count sentiment indicators
        for text in texts:
            text_lower = text.lower()
            positive_count += sum(1 for word in positive_words if word in text_lower)
            negative_count += sum(1 for word in negative_words if word in text_lower)
        
        total = positive_count + negative_count
        
        # Calculate sentiment
        if total == 0:
            sentiment = "neutral"
            score = 0.0
        else:
            score = (positive_count - negative_count) / total
            if score > 0.2:
                sentiment = "positive"
            elif score < -0.2:
                sentiment = "negative"
            else:
                sentiment = "neutral"
        
        result = {
            "sentiment": sentiment,
            "score": round(score, 2),
            "positive_signals": positive_count,
            "negative_signals": negative_count,
            "texts_analyzed": len(texts)
        }
        
        logger.info(f"Sentiment analysis for {market}: {sentiment} (score: {score:.2f})")
        return result
        
    except Exception as e:
        logger.error(f"Sentiment analysis error: {str(e)}")
        return {"status": "error", "message": str(e)}


def predict_price(data):
    """
    Simple price prediction using moving average and trend
    """
    try:
        prices = data.get('prices', [])
        market = data.get('market', 'UNKNOWN')
        prediction_days = data.get('prediction_days', 7)
        
        if len(prices) < 7:
            return {
                "status": "error",
                "message": "Need at least 7 price points for prediction"
            }
        
        # Calculate moving averages
        recent_avg = sum(prices[-7:]) / 7
        overall_avg = sum(prices) / len(prices)
        
        # Calculate trend factor
        trend_factor = (recent_avg - overall_avg) / overall_avg
        
        # Simple prediction
        current_price = prices[-1]
        predicted_price = current_price * (1 + trend_factor * 0.5)
        
        # Confidence based on data points
        if len(prices) > 30:
            confidence = "high"
        elif len(prices) > 14:
            confidence = "medium"
        else:
            confidence = "low"
        
        change_percent = ((predicted_price - current_price) / current_price) * 100
        
        result = {
            "current_price": round(current_price, 2),
            "predicted_price": round(predicted_price, 2),
            "prediction_days": prediction_days,
            "expected_change_percent": round(change_percent, 2),
            "confidence": confidence,
            "data_points_used": len(prices)
        }
        
        logger.info(f"Price prediction for {market}: ${predicted_price:.2f} ({confidence} confidence)")
        return result
        
    except Exception as e:
        logger.error(f"Price prediction error: {str(e)}")
        return {"status": "error", "message": str(e)}


def detect_anomalies(data):
    """
    Detect price anomalies using standard deviation
    """
    try:
        prices = data.get('prices', [])
        market = data.get('market', 'UNKNOWN')
        
        if len(prices) < 10:
            return {
                "status": "error",
                "message": "Need at least 10 price points for anomaly detection"
            }
        
        # Calculate statistics
        mean_price = statistics.mean(prices)
        std_dev = statistics.stdev(prices)
        
        # Find anomalies (>2 standard deviations)
        anomalies = []
        for i, price in enumerate(prices):
            z_score = abs((price - mean_price) / std_dev) if std_dev > 0 else 0
            
            if z_score > 2:
                deviation_percent = ((price - mean_price) / mean_price) * 100
                anomalies.append({
                    "index": i,
                    "price": round(price, 2),
                    "z_score": round(z_score, 2),
                    "deviation_percent": round(deviation_percent, 2)
                })
        
        result = {
            "anomalies_found": len(anomalies),
            "anomalies": anomalies[:5],  # Return top 5
            "mean_price": round(mean_price, 2),
            "std_deviation": round(std_dev, 2),
            "data_points_analyzed": len(prices)
        }
        
        logger.info(f"Anomaly detection for {market}: {len(anomalies)} anomalies found")
        return result
        
    except Exception as e:
        logger.error(f"Anomaly detection error: {str(e)}")
        return {"status": "error", "message": str(e)}


# API Endpoints

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint - confirms agent is alive"""
    response = {
        "status": "active",
        "agent_id": AGENT_CONFIG["agent_id"],
        "agent_name": AGENT_CONFIG["agent_name"],
        "version": AGENT_CONFIG["version"],
        "timestamp": datetime.now().isoformat()
    }
    logger.info("Health check requested")
    return jsonify(response), 200


@app.route('/info', methods=['GET'])
def agent_info():
    """Agent information endpoint - returns agent details"""
    response = {
        "agent_id": AGENT_CONFIG["agent_id"],
        "agent_name": AGENT_CONFIG["agent_name"],
        "version": AGENT_CONFIG["version"],
        "team": AGENT_CONFIG["team"],
        "capabilities": AGENT_CONFIG["capabilities"],
        "memory_stats": memory.get_stats(),
        "status": "ready",
        "timestamp": datetime.now().isoformat()
    }
    logger.info("Info requested")
    return jsonify(response), 200


@app.route('/analyze', methods=['POST'])
def analyze():
    """Main analysis endpoint - processes requests based on type"""
    try:
        # Get request data
        data = request.get_json()
        
        if not data:
            return jsonify({
                "status": "error",
                "message": "No data provided"
            }), 400
        
        # Generate task ID
        task_id = str(uuid.uuid4())
        analysis_type = data.get('type', 'trend')
        market = data.get('market', 'UNKNOWN')
        
        logger.info(f"Analysis request - Type: {analysis_type}, Market: {market}, Task: {task_id}")
        
        # Store in short-term memory
        memory.add_short_term({
            'task_id': task_id,
            'type': analysis_type,
            'market': market
        })
        
        # Route to appropriate analysis function
        if analysis_type == 'trend':
            analysis_result = analyze_trend(data)
        elif analysis_type == 'sentiment':
            analysis_result = analyze_sentiment(data)
        elif analysis_type == 'prediction':
            analysis_result = predict_price(data)
        elif analysis_type == 'anomaly':
            analysis_result = detect_anomalies(data)
        else:
            return jsonify({
                "status": "error",
                "message": f"Unknown analysis type: {analysis_type}"
            }), 400
        
        # Check if analysis had error
        if analysis_result.get('status') == 'error':
            return jsonify({
                "task_id": task_id,
                "status": "error",
                "message": analysis_result.get('message'),
                "agent_id": AGENT_CONFIG["agent_id"],
                "timestamp": datetime.now().isoformat()
            }), 400
        
        # Store successful analysis in long-term memory
        memory.add_long_term({
            'task_id': task_id,
            'type': analysis_type,
            'market': market,
            'result': analysis_result
        })
        
        # Build response
        response = {
            "task_id": task_id,
            "status": "success",
            "agent_id": AGENT_CONFIG["agent_id"],
            "market": market,
            "analysis_type": analysis_type,
            "result": analysis_result,
            "timestamp": datetime.now().isoformat()
        }
        
        logger.info(f"Analysis completed - Task: {task_id}")
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Analysis endpoint error: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e),
            "agent_id": AGENT_CONFIG["agent_id"],
            "timestamp": datetime.now().isoformat()
        }), 500


# Main entry point
if __name__ == '__main__':
    logger.info("=" * 60)
    logger.info("MARKET TREND MONITOR AGENT - STARTING")
    logger.info("=" * 60)
    logger.info(f"Agent ID: {AGENT_CONFIG['agent_id']}")
    logger.info(f"Agent Name: {AGENT_CONFIG['agent_name']}")
    logger.info(f"Version: {AGENT_CONFIG['version']}")
    logger.info("Team: Abdul Hannan, Agha Ahsan, Minahil Asif")
    logger.info("=" * 60)
    logger.info("Endpoints:")
    logger.info("  GET  /health  - Health check")
    logger.info("  GET  /info    - Agent information")
    logger.info("  POST /analyze - Main analysis endpoint")
    import os
    port = int(os.environ.get('PORT', 5000))
    logger.info("=" * 60)
    logger.info(f"Server starting on port {port}")
    logger.info("=" * 60)
    
    app.run(host='0.0.0.0', port=port, debug=False)
