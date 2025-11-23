# Quick Start Guide

## 🚀 How to Run the Agent

### Step 1: Install Python Dependencies

```powershell
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- requests (for testing)

---

### Step 2: Start the Agent

```powershell
python agent.py
```

You should see:
```
============================================================
MARKET TREND MONITOR AGENT - STARTING
============================================================
Agent ID: market-trend-agent-001
Agent Name: Market Trend Monitor
Version: 1.0.0
Team: Abdul Hannan, Agha Ahsan, Minahil Asif
============================================================
Endpoints:
  GET  /health  - Health check
  GET  /info    - Agent information
  POST /analyze - Main analysis endpoint
============================================================
Server starting on http://localhost:5000
============================================================
```

✅ **Your agent is now running!**

---

### Step 3: Test the Agent

**Option A: Run Automated Tests**
```powershell
python test_agent.py
```

**Option B: Manual Test with cURL**
```powershell
# Health check
curl http://localhost:5000/health

# Get agent info
curl http://localhost:5000/info

# Test trend analysis
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d "{\"type\":\"trend\",\"market\":\"BTC/USD\",\"prices\":[45000,46000,47000],\"volumes\":[1000000,1100000,1200000]}"
```

---

## 📋 For Supervisor Integration Sheet

Fill in these details:

| Column | Value |
|--------|-------|
| **A: Agent Name** | Market Trend Monitor Agent |
| **B: GitHub Link** | https://github.com/Minahilasif12/MarketTrendMonitorAgent |
| **C: API Testing Link** | https://github.com/Minahilasif12/MarketTrendMonitorAgent/blob/main/API_EXAMPLES.md |
| **D: Input Data** | See AGENT_DETAILS.md for sample JSON |
| **E: Output Data** | See AGENT_DETAILS.md for sample responses |

---

## 🐛 Troubleshooting

### "Port 5000 already in use"
```powershell
# Find what's using port 5000
netstat -ano | findstr :5000

# Kill that process
taskkill /PID <PID_NUMBER> /F
```

### "Module not found: requests"
```powershell
pip install requests
```

### "Module not found: Flask"
```powershell
pip install Flask
```

---

## 📁 Files Overview

```
spm-a4/
├── agent.py              # Main agent code (RUN THIS)
├── test_agent.py         # Automated tests
├── requirements.txt      # Dependencies
├── README.md            # Full documentation
├── API_EXAMPLES.md      # API examples with cURL
├── AGENT_DETAILS.md     # Details for supervisor sheet
└── QUICKSTART.md        # This file
```

---

## ✅ Verification Checklist

Before submitting, verify:

- [ ] Agent starts without errors (`python agent.py`)
- [ ] Health check works (`curl http://localhost:5000/health`)
- [ ] Info endpoint works (`curl http://localhost:5000/info`)
- [ ] All tests pass (`python test_agent.py`)
- [ ] GitHub repo is public and accessible
- [ ] README.md is clear and complete

---

## 📞 Need Help?

**Team Lead:** Abdul Hannan (22i-2441)  
**GitHub:** https://github.com/Minahilasif12/MarketTrendMonitorAgent
