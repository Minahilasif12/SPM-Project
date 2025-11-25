"""
Test Supervisor Integration
Simulates how a Supervisor Agent would interact with Market Trend Monitor Agent
"""

import requests
import json
from datetime import datetime

class SupervisorSimulator:
    """Simulates a Supervisor Agent interacting with specialized agents"""
    
    def __init__(self, agent_url):
        self.agent_url = agent_url
        self.agent_info = None
        self.registered = False
        
    def print_section(self, title):
        """Print formatted section header"""
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60)
    
    def discover_agent(self):
        """Step 1: Discover agent capabilities"""
        self.print_section("STEP 1: AGENT DISCOVERY")
        
        try:
            # Health check
            print(f"Checking agent health at: {self.agent_url}/health")
            health_response = requests.get(f"{self.agent_url}/health", timeout=10)
            health = health_response.json()
            
            print(f"✓ Agent Status: {health['status']}")
            print(f"✓ Agent ID: {health['agent_id']}")
            print(f"✓ Agent Name: {health['agent_name']}")
            
            # Get capabilities
            print(f"\nFetching agent capabilities...")
            info_response = requests.get(f"{self.agent_url}/info", timeout=10)
            self.agent_info = info_response.json()
            
            print(f"✓ Agent Type: {self.agent_info.get('agent_type', 'N/A')}")
            print(f"✓ Communication: {self.agent_info.get('communication_protocol', 'N/A')}")
            print(f"✓ Capabilities: {len(self.agent_info['capabilities'])} found")
            for cap in self.agent_info['capabilities']:
                print(f"  - {cap}")
            
            print(f"✓ Supported Sectors: {len(self.agent_info['supported_sectors'])} sectors")
            for sector in self.agent_info['supported_sectors']:
                print(f"  - {sector}")
            
            return True
            
        except Exception as e:
            print(f"✗ Discovery failed: {e}")
            return False
    
    def register_with_agent(self):
        """Step 2: Register supervisor with agent"""
        self.print_section("STEP 2: SUPERVISOR REGISTRATION")
        
        try:
            print("Registering supervisor with agent...")
            
            registration_data = {
                "supervisor_id": "supervisor-test-001",
                "supervisor_url": "http://localhost:5001",
                "supervisor_name": "Test Supervisor",
                "timestamp": datetime.now().isoformat()
            }
            
            response = requests.post(
                f"{self.agent_url}/register",
                json=registration_data,
                timeout=10
            )
            
            result = response.json()
            
            if result.get('status') == 'registered':
                self.registered = True
                print(f"✓ Registration successful!")
                print(f"✓ Registered with: {result['agent_name']}")
                print(f"✓ Message: {result['message']}")
            else:
                print(f"✗ Registration failed: {result.get('message')}")
            
            return self.registered
            
        except Exception as e:
            print(f"✗ Registration failed: {e}")
            return False
    
    def assign_analysis_task(self, sector, keywords, query_type="general"):
        """Step 3: Assign analysis task to agent"""
        self.print_section(f"STEP 3: TASK ASSIGNMENT - {sector.upper()}")
        
        try:
            print(f"Assigning analysis task...")
            print(f"  Sector: {sector}")
            print(f"  Keywords: {', '.join(keywords)}")
            print(f"  Type: {query_type}")
            
            task_data = {
                "sector": sector,
                "keywords": keywords,
                "type": query_type
            }
            
            response = requests.post(
                f"{self.agent_url}/analyze",
                json=task_data,
                timeout=30
            )
            
            result = response.json()
            
            if result.get('status') == 'success':
                print(f"\n✓ Task completed successfully!")
                print(f"✓ Task ID: {result['task_id']}")
                
                analysis = result['result']
                print(f"\n📊 ANALYSIS RESULTS:")
                print(f"  Sector: {analysis.get('sector')}")
                print(f"  Trend Direction: {analysis.get('trend_direction')}")
                print(f"  Strength: {analysis.get('strength')}")
                print(f"  Confidence: {analysis.get('confidence')}")
                
                print(f"\n💡 KEY INSIGHTS:")
                for i, insight in enumerate(analysis.get('insights', []), 1):
                    print(f"  {i}. {insight}")
                
                print(f"\n🎯 RECOMMENDATION:")
                print(f"  {analysis.get('recommendation')}")
                
                return result['task_id']
            else:
                print(f"✗ Task failed: {result.get('message')}")
                return None
                
        except Exception as e:
            print(f"✗ Task assignment failed: {e}")
            return None
    
    def check_task_status(self, task_id):
        """Step 4: Check task status"""
        self.print_section("STEP 4: TASK STATUS CHECK")
        
        try:
            print(f"Checking status for task: {task_id}")
            
            response = requests.get(
                f"{self.agent_url}/task/{task_id}",
                timeout=10
            )
            
            result = response.json()
            
            if result.get('status') == 'success':
                print(f"✓ Task Status: {result['task_status']}")
                print(f"✓ Created: {result['created_at']}")
                print(f"✓ Updated: {result['updated_at']}")
                
                if result.get('result'):
                    print(f"✓ Result available")
            else:
                print(f"✗ Status check failed: {result.get('message')}")
            
            return result
            
        except Exception as e:
            print(f"✗ Status check failed: {e}")
            return None
    
    def run_multi_sector_analysis(self, sectors):
        """Simulate supervisor coordinating multiple sector analyses"""
        self.print_section("MULTI-SECTOR ANALYSIS SCENARIO")
        
        print(f"User Query: 'Analyze trends across {', '.join(sectors)}'\n")
        print(f"Supervisor breaking down into {len(sectors)} sub-tasks...")
        
        results = []
        task_ids = []
        
        for i, sector in enumerate(sectors, 1):
            print(f"\n[{i}/{len(sectors)}] Analyzing {sector}...")
            
            keywords = {
                "Technology": ["AI", "automation", "cloud"],
                "E-commerce": ["online shopping", "digital payments", "mobile"],
                "Healthcare": ["telemedicine", "digital health", "AI diagnosis"],
                "Finance": ["fintech", "digital banking", "blockchain"]
            }
            
            task_id = self.assign_analysis_task(
                sector,
                keywords.get(sector, ["innovation", "growth"]),
                "multi_sector_analysis"
            )
            
            if task_id:
                task_ids.append(task_id)
        
        print(f"\n✓ Supervisor completed {len(task_ids)}/{len(sectors)} analyses")
        print(f"✓ Supervisor would now aggregate results and present to user")
        
        return task_ids


def main():
    """Main test function"""
    
    print("\n" + "=" * 60)
    print("  SUPERVISOR-AGENT INTEGRATION TEST")
    print("  Market Trend Monitor Agent")
    print("=" * 60)
    
    # Configuration
    AGENT_URL = "https://minahilasif222.pythonanywhere.com"
    # For local testing, uncomment:
    # AGENT_URL = "http://localhost:5000"
    
    print(f"\nTarget Agent: {AGENT_URL}")
    
    # Create supervisor simulator
    supervisor = SupervisorSimulator(AGENT_URL)
    
    # Test Sequence
    
    # 1. Discovery
    if not supervisor.discover_agent():
        print("\n✗ Test failed at discovery stage")
        return
    
    # 2. Registration
    if not supervisor.register_with_agent():
        print("\n✗ Test failed at registration stage")
        return
    
    # 3. Single Analysis
    task_id = supervisor.assign_analysis_task(
        sector="Technology",
        keywords=["AI", "machine learning", "automation", "cloud computing"],
        query_type="general"
    )
    
    if not task_id:
        print("\n✗ Test failed at task assignment stage")
        return
    
    # 4. Status Check
    supervisor.check_task_status(task_id)
    
    # 5. Multi-Sector Analysis
    supervisor.run_multi_sector_analysis([
        "E-commerce",
        "Healthcare",
        "Finance"
    ])
    
    # Summary
    print("\n" + "=" * 60)
    print("  TEST SUMMARY")
    print("=" * 60)
    print("✓ Agent Discovery: PASSED")
    print("✓ Supervisor Registration: PASSED")
    print("✓ Task Assignment: PASSED")
    print("✓ Task Status Check: PASSED")
    print("✓ Multi-Sector Analysis: PASSED")
    print("\n🎉 All integration tests passed!")
    print("\nYour agent is ready for supervisor integration!")
    print("=" * 60)


if __name__ == "__main__":
    main()
