# Supervisor Integration Guide
## Market Trend Monitor Agent

This guide explains how the Supervisor Agent interacts with your Market Trend Monitor Agent in a Multi-Agent System.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      SUPERVISOR AGENT                        │
│  (Coordinates multiple specialist agents)                   │
│                                                              │
│  - Receives user requests                                   │
│  - Routes tasks to appropriate agents                       │
│  - Aggregates results                 V                      │
│  - Manages workflow                                         │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ HTTP API Calls
                 │
      ┌──────────┴──────────┬──────────────┬──────────────┐
      │                     │              │              │
┌─────▼──────┐    ┌────────▼───────┐   ┌──▼───────┐   ┌──▼────────┐
│  MARKET    │    │  SENTIMENT     │   │  DATA    │   │  OTHER    │
│  TREND     │    │  ANALYSIS      │   │  SCRAPER │   │  AGENTS   │
│  MONITOR   │    │  AGENT         │   │  AGENT   │   │           │
│ (YOUR AGENT)│   │ (Classmate's)  │   │          │   │           │
└────────────┘    └────────────────┘   └──────────┘   └───────────┘
```

---

## How Supervisor Interacts With Your Agent

### 1. **Discovery & Registration**
When the Supervisor starts, it discovers available agents:

```python
# Supervisor code:
import requests

# Step 1: Check if agent is alive
health = requests.get("https://minahilasif222.pythonanywhere.com/health")
# Returns: {"status": "active", "agent_id": "market-trend-monitor-001"}

# Step 2: Get agent capabilities
info = requests.get("https://minahilasif222.pythonanywhere.com/info")
# Returns: capabilities, supported_sectors, endpoints

# Step 3: Register with your agent
registration = requests.post(
    "https://minahilasif222.pythonanywhere.com/register",
    json={
        "supervisor_id": "supervisor-001",
        "supervisor_url": "https://supervisor.example.com"
    }
)
```

### 2. **Task Assignment**
When user asks: *"What are the technology trends right now?"*

```python
# Supervisor receives request
# Supervisor thinks: "This needs market trend analysis"
# Supervisor routes to your agent:

response = requests.post(
    "https://minahilasif222.pythonanywhere.com/analyze",
    json={
        "sector": "Technology",
        "keywords": ["AI", "cloud", "automation"],
        "type": "general"
    }
)

result = response.json()
# Supervisor receives your analysis and presents to user
```

### 3. **Task Tracking**
Supervisor can monitor task progress:

```python
# After assigning task, supervisor gets task_id
task_id = "123e4567-e89b-12d3-a456-426614174000"

# Check status later
status = requests.get(
    f"https://minahilasif222.pythonanywhere.com/task/{task_id}"
)
# Returns: {"task_status": "completed", "result": {...}}
```

---

## Communication Protocol

### Available Endpoints for Supervisor

| Endpoint | Method | Purpose | Request | Response |
|----------|--------|---------|---------|----------|
| `/health` | GET | Check if agent is alive | None | `{"status": "active"}` |
| `/info` | GET | Get capabilities | None | Full agent info |
| `/register` | POST | Register supervisor | `{"supervisor_id": "..."}` | Registration confirmation |
| `/analyze` | POST | Request analysis | `{"sector": "...", "keywords": [...]}` | Analysis result + task_id |
| `/task/<id>` | GET | Check task status | None | Task status + result |

### Example: Complete Interaction Flow

```python
# Supervisor's complete workflow:

# 1. User asks: "Analyze e-commerce and healthcare trends"
user_query = "Analyze e-commerce and healthcare trends"

# 2. Supervisor breaks down into sub-tasks
tasks = [
    {"agent": "market-trend-monitor-001", "sector": "E-commerce"},
    {"agent": "market-trend-monitor-001", "sector": "Healthcare"}
]

# 3. Supervisor calls your agent twice
results = []

for task in tasks:
    response = requests.post(
        "https://minahilasif222.pythonanywhere.com/analyze",
        json={
            "sector": task["sector"],
            "keywords": ["growth", "digital", "innovation"],
            "type": "general"
        }
    )
    results.append(response.json())

# 4. Supervisor aggregates results
final_report = supervisor.aggregate(results)

# 5. Supervisor presents to user
print(final_report)
```

---

## What Supervisor Expects From Your Agent

### ✅ Must Have:
1. **Consistent Response Format**
   ```json
   {
     "task_id": "uuid",
     "status": "success",
     "agent_id": "market-trend-monitor-001",
     "result": { ... }
   }
   ```

2. **Error Handling**
   ```json
   {
     "status": "error",
     "message": "Clear error description",
     "agent_id": "market-trend-monitor-001"
   }
   ```

3. **Capability Declaration**
   - Your `/info` endpoint clearly states what you can do
   - Supervisor reads this to decide when to use you

4. **Reliability**
   - Your agent must respond within reasonable time (< 30 seconds)
   - Handle errors gracefully
   - Fallback mode when API fails

---

## Multi-Agent Collaboration Example

**User Query:** *"I want to launch a fintech startup. What should I know?"*

**Supervisor's Plan:**
1. **Route to Market Trend Agent (YOU)**: Analyze Finance sector trends
2. **Route to Sentiment Agent**: Analyze public sentiment about fintech
3. **Route to Data Scraper Agent**: Get latest fintech news
4. **Supervisor aggregates** all results into comprehensive report

**Your Agent's Role:**
```python
# Supervisor → Your Agent
POST /analyze
{
  "sector": "Finance",
  "keywords": ["fintech", "digital banking", "blockchain"],
  "type": "startup_insights"
}

# Your Agent → Supervisor
{
  "task_id": "abc123",
  "status": "success",
  "result": {
    "trend_direction": "Rising",
    "strength": "Strong",
    "insights": [
      "Digital banking adoption accelerating",
      "Blockchain integration increasing",
      "Regulatory landscape evolving"
    ],
    "recommendation": "Strong opportunity in mobile payment solutions"
  }
}
```

---

## Configuration for Your Team Spreadsheet

When filling your project spreadsheet, include:

```
Agent Name: Market Trend Monitor Agent
Agent ID: market-trend-monitor-001
Agent Type: Specialist
Capabilities: sector_trend_analysis, emerging_pattern_detection, 
              business_insight_generation, trend_forecasting
Communication: REST API
Base URL: https://minahilasif222.pythonanywhere.com

Endpoints:
- GET  /health     → Health check
- GET  /info       → Capabilities
- POST /register   → Supervisor registration
- POST /analyze    → Main analysis function
- GET  /task/<id>  → Task status

Supported Sectors: Technology, E-commerce, Healthcare, Sustainability,
                   Finance, Education, Manufacturing, Retail

Integration: HTTP/REST - Supervisor calls endpoints, receives JSON responses
```

---

## Testing Supervisor Integration

Create a simple supervisor simulation:

```python
# test_supervisor.py
import requests

class SimpleSupervisor:
    def __init__(self):
        self.agent_url = "https://minahilasif222.pythonanywhere.com"
        self.agent_id = None
        
    def discover_agent(self):
        """Discover and register with agent"""
        # Health check
        health = requests.get(f"{self.agent_url}/health")
        print("Health:", health.json())
        
        # Get capabilities
        info = requests.get(f"{self.agent_url}/info")
        agent_info = info.json()
        self.agent_id = agent_info['agent_id']
        print(f"Discovered: {agent_info['agent_name']}")
        print(f"Capabilities: {agent_info['capabilities']}")
        
        # Register
        reg = requests.post(f"{self.agent_url}/register", json={
            "supervisor_id": "test-supervisor-001",
            "supervisor_url": "http://localhost:5001"
        })
        print("Registration:", reg.json())
        
    def assign_task(self, sector, query):
        """Assign analysis task to agent"""
        response = requests.post(f"{self.agent_url}/analyze", json={
            "sector": sector,
            "keywords": query.split(),
            "type": "general"
        })
        
        result = response.json()
        print(f"\nTask ID: {result['task_id']}")
        print(f"Analysis: {result['result']}")
        
        return result['task_id']
    
    def check_task(self, task_id):
        """Check task status"""
        status = requests.get(f"{self.agent_url}/task/{task_id}")
        print(f"\nTask Status: {status.json()}")

# Test
supervisor = SimpleSupervisor()
supervisor.discover_agent()

# Assign task
task_id = supervisor.assign_task("Technology", "AI cloud automation")

# Check task
supervisor.check_task(task_id)
```

---

## Summary

**Your Agent:**
- Runs independently at https://minahilasif222.pythonanywhere.com
- Exposes REST API endpoints
- Provides market trend analysis capabilities

**Supervisor Agent:**
- Discovers your agent via `/health` and `/info`
- Registers with your agent via `/register`
- Sends analysis requests to `/analyze`
- Tracks tasks via `/task/<id>`
- Combines your results with other agents

**Communication:** Pure HTTP/REST - language and framework independent!

Your agent is now **supervisor-ready**! 🎉
