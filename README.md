# Business Trend Monitor Agent

AI-powered agent that analyzes emerging business trends across various sectors using Google Gemini API.

## 🎯 Project Overview

**Agent Name**: Business Trend Monitor Agent  
**Purpose**: Continuously scans and analyzes business trends to provide adaptive insights  
**Team**: Abdul Hannan (PM), Agha Ahsan (Data & QA), Minahil Asif (Lead Dev)  
**Course**: Software Project Management (Dr. Behjat Zuhaira, Section D)

## ✨ Features

- **Multi-Sector Analysis**: Technology, E-commerce, Healthcare, Sustainability, Finance, Education, Manufacturing, Retail
- **AI-Powered Insights**: Uses Google Gemini 1.5 Flash for advanced trend analysis
- **Fallback Mode**: Works without API key using intelligent keyword analysis
- **Memory Management**: Tracks recent analyses (50 short-term, 1000 long-term)
- **RESTful API**: JSON-based communication for supervisor integration

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key (Optional but Recommended)

Get your free Gemini API key: https://makersuite.google.com/app/apikey

```bash
# Copy example file
cp .env.example .env

# Edit .env and add your key
GEMINI_API_KEY=your_actual_key_here
```

**Note**: Agent works in fallback mode without API key, but AI analysis provides better insights!

### 3. Run the Agent

```bash
python agent.py
```

Server starts on http://localhost:5000

### 4. Test the Agent

```bash
# In a new terminal
python test_agent.py
```

## 📡 API Endpoints

### GET /health

Health check endpoint

**Response**:
```json
{
  "status": "active",
  "agent_id": "business-trend-monitor-001",
  "agent_name": "Business Trend Monitor Agent",
  "version": "2.0.0",
  "gemini_status": "connected",
  "timestamp": "2025-11-24T..."
}
```

### GET /info

Agent information and capabilities

**Response**:
```json
{
  "agent_id": "business-trend-monitor-001",
  "agent_name": "Business Trend Monitor Agent",
  "version": "2.0.0",
  "description": "Analyzes emerging business trends across various sectors",
  "team": [...],
  "capabilities": ["sector_trend_analysis", "emerging_pattern_detection", ...],
  "supported_sectors": ["Technology", "E-commerce", "Healthcare", ...],
  "memory_stats": {...}
}
```

### POST /analyze

Analyze business trends in a specific sector

**Request**:
```json
{
  "sector": "Technology",
  "keywords": ["AI", "automation", "cloud computing"],
  "type": "emerging_trends"
}
```

**Response**:
```json
{
  "task_id": "uuid",
  "status": "success",
  "agent_id": "business-trend-monitor-001",
  "sector": "Technology",
  "analysis_type": "emerging_trends",
  "result": {
    "sector": "Technology",
    "trend_direction": "Rising",
    "strength": "Strong",
    "confidence": 0.85,
    "key_patterns": ["AI adoption", "automation growth", "cloud migration"],
    "insights": [
      "AI and automation adoption increasing rapidly",
      "Cloud computing becoming essential infrastructure",
      "Digital transformation accelerating across industries"
    ],
    "recommendation": "Invest in AI capabilities and cloud infrastructure"
  },
  "timestamp": "2025-11-24T..."
}
```

## 🏢 Supported Sectors

1. **Technology** - AI, automation, cloud computing
2. **E-commerce** - Online shopping, mobile commerce
3. **Healthcare** - Telemedicine, digital health
4. **Sustainability** - Green business, renewable energy
5. **Finance** - Digital banking, fintech
6. **Education** - Online learning, EdTech
7. **Manufacturing** - Industry 4.0, automation
8. **Retail** - Omnichannel, customer experience

## 🧠 How It Works

1. **Input**: Receives sector name and business keywords
2. **AI Analysis**: Uses Google Gemini to analyze trends (or fallback logic)
3. **Pattern Detection**: Identifies emerging patterns and business implications
4. **Insight Generation**: Produces actionable business insights
5. **Memory Storage**: Saves analysis for future reference
6. **JSON Output**: Returns structured results to supervisor

## 📊 Analysis Types

- `emerging_trends` - Detect new patterns
- `market_analysis` - Market movement insights
- `innovation_tracking` - Technology adoption
- `trend_forecast` - Future predictions
- `general` - Comprehensive analysis

## 🔧 Technical Stack

- **Framework**: Flask 3.0.0
- **AI Model**: Google Gemini 1.5 Flash (free tier)
- **Language**: Python 3.8+
- **Memory**: In-memory (deque + list)
- **Logging**: File + Console

## 📁 Project Structure

```
spm-a4/
├── agent.py              # Main agent implementation
├── test_agent.py         # Integration tests
├── requirements.txt      # Python dependencies
├── .env.example          # API key template
├── README.md             # This file
└── agent.log             # Runtime logs
```

## 🧪 Testing

Run all integration tests:

```bash
python test_agent.py
```

Tests cover:
- Health check
- Agent info
- Technology sector analysis
- E-commerce sector analysis
- Healthcare sector analysis
- Sustainability sector analysis

Expected: **6/6 tests passed (100%)**

## 🌐 Deployment

**Live URL**: https://minahilasif222.pythonanywhere.com

Deployed on PythonAnywhere (free tier)

Test live agent:
```bash
curl https://minahilasif222.pythonanywhere.com/health
```

## 📝 Example Usage

```bash
# Analyze Technology trends
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "sector": "Technology",
    "keywords": ["AI", "automation", "cloud"],
    "type": "emerging_trends"
  }'

# Analyze Healthcare trends
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "sector": "Healthcare",
    "keywords": ["telemedicine", "digital health"],
    "type": "innovation_tracking"
  }'
```

## 🔐 Security Notes

- Uses free public API (Google Gemini)
- No sensitive data storage
- No PII collection
- Rate limits: 15 requests/minute (Gemini free tier)

## 👥 Team

- **Abdul Hannan** (22i-2441) - Project Manager
- **Agha Ahsan** (22i-1117) - Data & Testing Lead
- **Minahil Asif** (22i-2710) - Lead Developer

## 📚 Course Information

**Course**: Fundamentals of Software Project Management  
**Instructor**: Dr. Behjat Zuhaira  
**Section**: D  
**Semester**: Fall 2025  
**Institution**: FAST NUCES

## 📄 License

Academic Project - FAST NUCES © 2025

## 🔗 Repository

GitHub: https://github.com/Minahilasif12/MarketTrendMonitorAgent
