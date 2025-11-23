# Market Trend Monitor Agent

**Simple AI Worker Agent for Market Trend Analysis**

---

## 👥 Team Information

| Name | Roll Number | Role |
|------|-------------|------|
| Abdul Hannan | 22i-2441 | Project Manager |
| Agha Ahsan | 22i-1117 | Data & Testing Lead |
| Minahil Asif | 22i-2710 | Lead Developer |

**Course:** Fundamentals of Software Project Management  
**Instructor:** Dr. Behjat Zuhaira  
**Section:** D  
**Deadline:** November 30, 2025

---

## 🎯 Project Overview

The **Market Trend Monitor Agent** is a lightweight AI worker agent that analyzes market data and provides insights on:

- 📈 **Trend Analysis** - Identify bullish, bearish, or neutral trends
- 💬 **Sentiment Analysis** - Analyze market sentiment from text
- 🔮 **Price Prediction** - Predict future price movements
- ⚠️ **Anomaly Detection** - Detect unusual market patterns

### Key Features

✅ Simple Python implementation (no complex dependencies)  
✅ JSON API for easy integration  
✅ Works with Supervisor-Worker architecture  
✅ Built-in memory management (short-term & long-term)  
✅ Comprehensive logging  
✅ Health monitoring  

---

## 🏗️ Architecture

```
        SUPERVISOR (Provided by FAST)
                    ↓
            JSON Request
                    ↓
    ┌───────────────────────────────┐
    │  MARKET TREND MONITOR AGENT   │
    │  (Our Implementation)         │
    │                               │
    │  • Trend Analysis             │
    │  • Sentiment Analysis         │
    │  • Price Prediction           │
    │  • Anomaly Detection          │
    │  • Memory Management          │
    └───────────────────────────────┘
                    ↓
            JSON Response
                    ↓
        SUPERVISOR (Provided by FAST)
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Navigate to project folder:**
   ```powershell
   cd C:\Users\DELL\Downloads\spm-a4
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the agent:**
   ```powershell
   python agent.py
   ```

4. **Verify it's running:**
   ```powershell
   curl http://localhost:5000/health
   ```

---

## 📡 API Endpoints

### 1. Health Check

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "active",
  "agent_id": "market-trend-agent-001",
  "agent_name": "Market Trend Monitor",
  "version": "1.0.0",
  "timestamp": "2025-11-23T10:30:00"
}
```

---

### 2. Agent Information

**Endpoint:** `GET /info`

**Response:**
```json
{
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
  ],
  "memory_stats": {
    "short_term_count": 15,
    "long_term_count": 42
  },
  "status": "ready"
}
```

---

### 3. Main Analysis Endpoint

**Endpoint:** `POST /analyze`

**Content-Type:** `application/json`

---

#### 📈 Trend Analysis

**Request:**
```json
{
  "type": "trend",
  "market": "BTC/USD",
  "prices": [45000, 45500, 46000, 45800, 46500, 47000],
  "volumes": [1200000, 1300000, 1250000, 1400000, 1350000, 1450000]
}
```

**Response:**
```json
{
  "task_id": "abc-123-def",
  "status": "success",
  "agent_id": "market-trend-agent-001",
  "market": "BTC/USD",
  "analysis_type": "trend",
  "result": {
    "trend": "bullish",
    "strength": "moderate",
    "price_change_percent": 4.44,
    "current_price": 47000,
    "average_volume": 1325000,
    "insights": ["Strong upward momentum detected"]
  },
  "timestamp": "2025-11-23T10:35:00"
}
```

---

#### 💬 Sentiment Analysis

**Request:**
```json
{
  "type": "sentiment",
  "market": "ETH/USD",
  "texts": [
    "Bitcoin shows strong bullish momentum",
    "Market rally continues with high growth",
    "Investors profit from surge in prices"
  ]
}
```

**Response:**
```json
{
  "task_id": "xyz-456-abc",
  "status": "success",
  "agent_id": "market-trend-agent-001",
  "market": "ETH/USD",
  "analysis_type": "sentiment",
  "result": {
    "sentiment": "positive",
    "score": 0.85,
    "positive_signals": 9,
    "negative_signals": 0,
    "texts_analyzed": 3
  },
  "timestamp": "2025-11-23T10:40:00"
}
```

---

#### 🔮 Price Prediction

**Request:**
```json
{
  "type": "prediction",
  "market": "BTC/USD",
  "prices": [45000, 45500, 46000, 45800, 46500, 47000, 47200],
  "prediction_days": 7
}
```

**Response:**
```json
{
  "task_id": "pred-789-xyz",
  "status": "success",
  "agent_id": "market-trend-agent-001",
  "market": "BTC/USD",
  "analysis_type": "prediction",
  "result": {
    "current_price": 47200,
    "predicted_price": 48100,
    "prediction_days": 7,
    "expected_change_percent": 1.91,
    "confidence": "medium",
    "data_points_used": 7
  },
  "timestamp": "2025-11-23T10:45:00"
}
```

---

#### ⚠️ Anomaly Detection

**Request:**
```json
{
  "type": "anomaly",
  "market": "BTC/USD",
  "prices": [45000, 45500, 46000, 52000, 46500, 47000, 46800, 47200, 55000, 47500]
}
```

**Response:**
```json
{
  "task_id": "anom-012-def",
  "status": "success",
  "agent_id": "market-trend-agent-001",
  "market": "BTC/USD",
  "analysis_type": "anomaly",
  "result": {
    "anomalies_found": 2,
    "anomalies": [
      {
        "index": 3,
        "price": 52000,
        "z_score": 2.34,
        "deviation_percent": 11.5
      },
      {
        "index": 8,
        "price": 55000,
        "z_score": 3.21,
        "deviation_percent": 18.2
      }
    ],
    "mean_price": 46750,
    "std_deviation": 3200,
    "data_points_analyzed": 10
  },
  "timestamp": "2025-11-23T10:50:00"
}
```

---

## 🧪 Testing

### Run Integration Tests

```powershell
python test_agent.py
```

### Manual Testing with cURL

**Health Check:**
```powershell
curl http://localhost:5000/health
```

**Trend Analysis:**
```powershell
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d "{\"type\":\"trend\",\"market\":\"BTC/USD\",\"prices\":[45000,46000,47000],\"volumes\":[1000000,1100000,1200000]}"
```

**Agent Info:**
```powershell
curl http://localhost:5000/info
```

---

## 💾 Memory Strategy

### Short-Term Memory
- **Capacity:** 50 entries (automatically managed)
- **Purpose:** Track recent tasks and quick lookups
- **Storage:** In-memory deque (FIFO)

### Long-Term Memory
- **Capacity:** 1000 entries
- **Purpose:** Store successful analyses and patterns
- **Storage:** In-memory list with size management

---

## 📁 Project Structure

```
spm-a4/
├── agent.py              # Main worker agent (Flask API)
├── test_agent.py         # Integration tests
├── requirements.txt      # Python dependencies (Flask only)
├── README.md            # This file
└── agent.log            # Runtime logs (auto-generated)
```

---

## 📊 Rubric Compliance

| Requirement | Status | Implementation |
|------------|--------|----------------|
| **Functionality** | ✅ | 4 analysis types fully working |
| **Supervisor Integration** | ✅ | JSON API, health check, external callable |
| **Code Quality** | ✅ | Modular functions, clear documentation |
| **Deployment** | ✅ | Simple `pip install` + `python agent.py` |
| **Logging** | ✅ | Detailed logs to file and console |
| **Health Check** | ✅ | `/health` endpoint returns status |
| **Integration Testing** | ✅ | 6 comprehensive tests in test_agent.py |

---

## 🔧 Troubleshooting

### Port Already in Use
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Module Not Found
```powershell
pip install -r requirements.txt --force-reinstall
```

### Agent Not Responding
Check if agent is running:
```powershell
curl http://localhost:5000/health
```

---

## 📝 Logging

All activity is logged to:
- **Console:** Real-time output
- **File:** `agent.log` (persistent)

**Log Format:**
```
2025-11-23 10:30:00 - INFO - Analysis request - Type: trend, Market: BTC/USD
2025-11-23 10:30:01 - INFO - Trend analysis for BTC/USD: bullish (moderate)
2025-11-23 10:30:01 - INFO - Analysis completed - Task: abc-123-def
```

---

## 📞 Support

**Team Lead:** Abdul Hannan (22i-2441)  
**Course:** Fundamentals of Software Project Management  
**Instructor:** Dr. Behjat Zuhaira

---

**Last Updated:** November 23, 2025
