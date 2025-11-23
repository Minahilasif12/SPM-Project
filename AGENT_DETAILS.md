# Agent Details for Supervisor Integration

## 📋 Agent Information Sheet

**For submission to supervisor integration spreadsheet:**

---

### Column A: Agent Name
```
Market Trend Monitor Agent
```

---

### Column B: Deployed/Github link
```
https://github.com/Minahilasif12/MarketTrendMonitorAgent
```

---

### Column C: API Testing Link
```
https://github.com/Minahilasif12/MarketTrendMonitorAgent/blob/main/API_EXAMPLES.md
```

Or if deployed online:
```
http://your-deployment-url.com/info
```

---

### Column D: Input Data (Sample JSON)

**For Trend Analysis:**
```json
{
  "type": "trend",
  "market": "BTC/USD",
  "prices": [45000, 45500, 46000, 45800, 46500, 47000],
  "volumes": [1200000, 1300000, 1250000, 1400000, 1350000, 1450000]
}
```

**For Sentiment Analysis:**
```json
{
  "type": "sentiment",
  "market": "ETH/USD",
  "texts": [
    "Bitcoin shows strong bullish momentum",
    "Market rally continues with high growth"
  ]
}
```

**For Price Prediction:**
```json
{
  "type": "prediction",
  "market": "BTC/USD",
  "prices": [45000, 45500, 46000, 45800, 46500, 47000, 47200],
  "prediction_days": 7
}
```

**For Anomaly Detection:**
```json
{
  "type": "anomaly",
  "market": "BTC/USD",
  "prices": [45000, 45500, 46000, 52000, 46500, 47000, 55000, 47500]
}
```

---

### Column E: Output Data (Sample Response)

**Trend Analysis Response:**
```json
{
  "task_id": "abc-123-def-456",
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

**Sentiment Analysis Response:**
```json
{
  "task_id": "xyz-456-abc-789",
  "status": "success",
  "agent_id": "market-trend-agent-001",
  "market": "ETH/USD",
  "analysis_type": "sentiment",
  "result": {
    "sentiment": "positive",
    "score": 0.85,
    "positive_signals": 9,
    "negative_signals": 0,
    "texts_analyzed": 2
  },
  "timestamp": "2025-11-23T10:40:00"
}
```

---

## 🔗 API Endpoints

### Base URL (Local)
```
http://localhost:5000
```

### 1. Health Check
```
GET /health
```

### 2. Agent Info
```
GET /info
```

### 3. Analysis (Main Endpoint)
```
POST /analyze
Content-Type: application/json
```

---

## 🚀 How Supervisor Will Call Our Agent

The supervisor will make HTTP POST requests to our `/analyze` endpoint:

```bash
POST http://localhost:5000/analyze
Content-Type: application/json

{
  "type": "trend",
  "market": "BTC/USD",
  "prices": [...],
  "volumes": [...]
}
```

Our agent will respond with:
```json
{
  "task_id": "unique-id",
  "status": "success",
  "result": {...}
}
```

---

## 📞 Contact Information

**Team Lead:** Abdul Hannan (22i-2441)  
**Members:** Agha Ahsan (22i-1117), Minahil Asif (22i-2710)  
**Course:** Fundamentals of Software Project Management  
**Instructor:** Dr. Behjat Zuhaira  
**Section:** D
