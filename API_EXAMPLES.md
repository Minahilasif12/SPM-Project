# API Examples and Testing Guide

## 🔗 Base URL
```
http://localhost:5000
```

---

## 1️⃣ Health Check

**Endpoint:** `GET /health`

**cURL Command:**
```bash
curl http://localhost:5000/health
```

**Expected Response:**
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

## 2️⃣ Agent Information

**Endpoint:** `GET /info`

**cURL Command:**
```bash
curl http://localhost:5000/info
```

**Expected Response:**
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
  "status": "ready"
}
```

---

## 3️⃣ Trend Analysis

**Endpoint:** `POST /analyze`

**cURL Command:**
```bash
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d "{\"type\":\"trend\",\"market\":\"BTC/USD\",\"prices\":[45000,45500,46000,45800,46500,47000],\"volumes\":[1200000,1300000,1250000,1400000,1350000,1450000]}"
```

**Request Body:**
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
  "task_id": "unique-uuid",
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

## 4️⃣ Sentiment Analysis

**cURL Command:**
```bash
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d "{\"type\":\"sentiment\",\"market\":\"ETH/USD\",\"texts\":[\"Bitcoin shows strong bullish momentum\",\"Market rally continues\"]}"
```

**Request Body:**
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

**Response:**
```json
{
  "task_id": "unique-uuid",
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

## 5️⃣ Price Prediction

**cURL Command:**
```bash
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d "{\"type\":\"prediction\",\"market\":\"BTC/USD\",\"prices\":[45000,45500,46000,45800,46500,47000,47200],\"prediction_days\":7}"
```

**Request Body:**
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
  "task_id": "unique-uuid",
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

## 6️⃣ Anomaly Detection

**cURL Command:**
```bash
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d "{\"type\":\"anomaly\",\"market\":\"BTC/USD\",\"prices\":[45000,45500,46000,52000,46500,47000,55000,47500]}"
```

**Request Body:**
```json
{
  "type": "anomaly",
  "market": "BTC/USD",
  "prices": [45000, 45500, 46000, 52000, 46500, 47000, 55000, 47500]
}
```

**Response:**
```json
{
  "task_id": "unique-uuid",
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
      }
    ],
    "mean_price": 46750,
    "std_deviation": 3200,
    "data_points_analyzed": 8
  },
  "timestamp": "2025-11-23T10:50:00"
}
```

---

## 🧪 Python Testing

```python
import requests

# Test health
response = requests.get("http://localhost:5000/health")
print(response.json())

# Test trend analysis
payload = {
    "type": "trend",
    "market": "BTC/USD",
    "prices": [45000, 46000, 47000],
    "volumes": [1000000, 1100000, 1200000]
}
response = requests.post("http://localhost:5000/analyze", json=payload)
print(response.json())
```

---

## ✅ Quick Verification

Run these commands to verify your agent is working:

```bash
# 1. Health check
curl http://localhost:5000/health

# 2. Get info
curl http://localhost:5000/info

# 3. Simple trend test
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d "{\"type\":\"trend\",\"market\":\"TEST\",\"prices\":[100,105,110],\"volumes\":[1000,1100,1200]}"
```

All should return JSON responses with `"status": "success"` or `"status": "active"`.
