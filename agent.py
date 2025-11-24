"""
Market Trend Monitor Agent - Business Trend Analysis
Analyzes emerging business trends across various sectors using AI
Team: Abdul Hannan, Agha Ahsan, Minahil Asif
"""

from flask import Flask, request, jsonify
import os
import json
import logging
from datetime import datetime
from collections import deque
import uuid

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not required, can use system env vars

# Google Generative AI - optional (fallback mode if not available)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    genai = None
    GEMINI_AVAILABLE = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agent.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Agent Configuration
AGENT_CONFIG = {
    "agent_id": "market-trend-monitor-001",
    "agent_name": "Market Trend Monitor Agent",
    "version": "2.0.0",
    "description": "Analyzes emerging market trends across various sectors",
    "team": [
        {"name": "Abdul Hannan", "role": "Project Manager", "roll": "22i-2441"},
        {"name": "Agha Ahsan", "role": "Data & Testing", "roll": "22i-1117"},
        {"name": "Minahil Asif", "role": "Lead Developer", "roll": "22i-2710"}
    ],
    "capabilities": [
        "sector_trend_analysis",
        "emerging_pattern_detection",
        "business_insight_generation",
        "trend_forecasting"
    ],
    "supported_sectors": [
        "Technology",
        "E-commerce",
        "Healthcare",
        "Sustainability",
        "Finance",
        "Education",
        "Manufacturing",
        "Retail"
    ]
}

# Configure Gemini API
def configure_gemini():
    """Configure Google Gemini API"""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        logger.warning("GEMINI_API_KEY not set - using fallback analysis mode")
        return None
    
    try:
        genai.configure(api_key=api_key)
        # Use stable model that supports generateContent
        model = genai.GenerativeModel('models/gemini-pro-latest')
        logger.info("Gemini API configured successfully (models/gemini-pro-latest)")
        return model
    except Exception as e:
        logger.error(f"Failed to configure Gemini: {e}")
        return None

# Initialize Gemini model
gemini_model = configure_gemini()

# Simple Memory Management
class SimpleMemory:
    def __init__(self):
        self.short_term = deque(maxlen=50)  # Last 50 analyses
        self.long_term = []  # Successful analyses (max 1000)
        
    def add_short_term(self, data):
        """Add to short-term memory"""
        self.short_term.append({
            'timestamp': datetime.now().isoformat(),
            'data': data
        })
    
    def add_long_term(self, data):
        """Add to long-term memory"""
        if len(self.long_term) < 1000:
            self.long_term.append({
                'timestamp': datetime.now().isoformat(),
                'data': data
            })
    
    def get_stats(self):
        """Get memory statistics"""
        return {
            "short_term_count": len(self.short_term),
            "short_term_capacity": 50,
            "long_term_count": len(self.long_term),
            "long_term_capacity": 1000
        }

# Initialize memory
memory = SimpleMemory()

# Fallback Analysis (when Gemini API not available)
def fallback_analysis(sector, keywords):
    """Simple keyword-based analysis when API unavailable"""
    
    # Trend keywords mapping
    positive_trends = ['growth', 'innovation', 'adoption', 'expansion', 'increase', 
                       'rising', 'emerging', 'digital', 'AI', 'automation', 'cloud',
                       'sustainable', 'green', 'remote', 'online']
    
    negative_trends = ['decline', 'reduction', 'traditional', 'offline', 'legacy']
    
    # Analyze keywords
    text = ' '.join(keywords).lower()
    positive_count = sum(1 for word in positive_trends if word in text)
    negative_count = sum(1 for word in negative_trends if word in text)
    
    # Determine trend
    if positive_count > negative_count:
        trend_direction = "Rising"
        strength = "Strong" if positive_count >= 3 else "Moderate"
    elif negative_count > positive_count:
        trend_direction = "Declining"
        strength = "Moderate"
    else:
        trend_direction = "Stable"
        strength = "Moderate"
    
    # Generate insights based on sector
    sector_insights = {
        "Technology": ["AI and automation adoption increasing", "Cloud computing growth"],
        "E-commerce": ["Mobile commerce expanding", "Personalization trending"],
        "Healthcare": ["Telemedicine adoption rising", "Digital health innovations"],
        "Sustainability": ["Green business practices growing", "Renewable energy focus"],
        "Finance": ["Digital banking expanding", "Fintech innovations"],
        "Education": ["Online learning growth", "EdTech adoption"],
        "Manufacturing": ["Industry 4.0 adoption", "Automation increasing"],
        "Retail": ["Omnichannel strategies", "Customer experience focus"]
    }
    
    insights = sector_insights.get(sector, ["Market evolution ongoing", "Digital transformation trending"])
    
    return {
        "sector": sector,
        "trend_direction": trend_direction,
        "strength": strength,
        "confidence": 0.65,
        "key_patterns": keywords[:3],
        "insights": insights,
        "recommendation": f"Monitor {sector} sector closely for emerging opportunities"
    }

# AI-Powered Analysis using Gemini
def analyze_with_gemini(sector, keywords, query_type="general"):
    """Use Gemini API for advanced trend analysis"""
    
    if not gemini_model:
        logger.info("Gemini not available, using fallback analysis")
        return fallback_analysis(sector, keywords)
    
    try:
        # Create analysis prompt
        prompt = f"""You are a business trend analyst. Analyze the following:

Sector: {sector}
Keywords/Indicators: {', '.join(keywords)}
Analysis Type: {query_type}

Provide a structured analysis in the following JSON format:
{{
    "trend_direction": "Rising/Declining/Stable",
    "strength": "Strong/Moderate/Weak",
    "confidence": 0.0-1.0,
    "key_patterns": ["pattern1", "pattern2", "pattern3"],
    "insights": ["insight1", "insight2", "insight3"],
    "recommendation": "Brief actionable recommendation"
}}

Focus on: emerging patterns, business implications, and actionable insights.
Keep insights concise and business-focused."""

        # Generate response
        response = gemini_model.generate_content(prompt)
        
        # Parse JSON response
        response_text = response.text.strip()
        
        # Extract JSON from markdown code blocks if present
        if '```json' in response_text:
            response_text = response_text.split('```json')[1].split('```')[0].strip()
        elif '```' in response_text:
            response_text = response_text.split('```')[1].split('```')[0].strip()
        
        result = json.loads(response_text)
        result['sector'] = sector
        
        logger.info(f"Gemini analysis successful for {sector}")
        return result
        
    except json.JSONDecodeError as e:
        logger.warning(f"JSON parse error from Gemini response: {e}")
        return fallback_analysis(sector, keywords)
    except Exception as e:
        logger.error(f"Gemini API error: {e}")
        return fallback_analysis(sector, keywords)

# Flask Routes

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    logger.info("Health check requested")
    
    return jsonify({
        "status": "active",
        "agent_id": AGENT_CONFIG["agent_id"],
        "agent_name": AGENT_CONFIG["agent_name"],
        "version": AGENT_CONFIG["version"],
        "gemini_status": "connected" if gemini_model else "fallback_mode",
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route('/info', methods=['GET'])
def agent_info():
    """Return agent information"""
    logger.info("Info requested")
    
    return jsonify({
        "agent_id": AGENT_CONFIG["agent_id"],
        "agent_name": AGENT_CONFIG["agent_name"],
        "version": AGENT_CONFIG["version"],
        "description": AGENT_CONFIG["description"],
        "team": AGENT_CONFIG["team"],
        "capabilities": AGENT_CONFIG["capabilities"],
        "supported_sectors": AGENT_CONFIG["supported_sectors"],
        "memory_stats": memory.get_stats(),
        "status": "ready",
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route('/analyze', methods=['POST'])
def analyze_trends():
    """Main analysis endpoint for business trend monitoring"""
    
    try:
        # Parse request
        data = request.get_json()
        
        if not data:
            return jsonify({
                "status": "error",
                "message": "No JSON data provided",
                "agent_id": AGENT_CONFIG["agent_id"],
                "timestamp": datetime.now().isoformat()
            }), 400
        
        # Extract parameters
        sector = data.get('sector', 'Technology')
        keywords = data.get('keywords', [])
        query_type = data.get('type', 'general')
        
        # Validate sector
        if sector not in AGENT_CONFIG["supported_sectors"]:
            return jsonify({
                "status": "error",
                "message": f"Unsupported sector. Supported: {', '.join(AGENT_CONFIG['supported_sectors'])}",
                "agent_id": AGENT_CONFIG["agent_id"],
                "timestamp": datetime.now().isoformat()
            }), 400
        
        # Generate task ID
        task_id = str(uuid.uuid4())
        
        logger.info(f"Analysis request - Sector: {sector}, Type: {query_type}, Task: {task_id}")
        
        # Perform analysis
        analysis_result = analyze_with_gemini(sector, keywords, query_type)
        
        # Store in memory
        memory.add_short_term({
            'task_id': task_id,
            'sector': sector,
            'type': query_type
        })
        
        memory.add_long_term({
            'task_id': task_id,
            'sector': sector,
            'result': analysis_result
        })
        
        # Build response
        response = {
            "task_id": task_id,
            "status": "success",
            "agent_id": AGENT_CONFIG["agent_id"],
            "sector": sector,
            "analysis_type": query_type,
            "result": analysis_result,
            "timestamp": datetime.now().isoformat()
        }
        
        logger.info(f"Analysis completed - Task: {task_id}, Trend: {analysis_result.get('trend_direction')}")
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
    logger.info("  POST /analyze - Market trend analysis")
    logger.info("=" * 60)
    logger.info(f"Gemini API: {'Enabled' if gemini_model else 'Disabled (Fallback Mode)'}")
    logger.info("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=False)
