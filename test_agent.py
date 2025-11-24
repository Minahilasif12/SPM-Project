"""
Integration Tests for Business Trend Monitor Agent
Tests all endpoints and business trend analysis functionality
"""

try:
    import requests
except ImportError:
    print("=" * 60)
    print("ERROR: 'requests' module not found")
    print("=" * 60)
    print("Please install it using:")
    print("  pip install requests")
    print("=" * 60)
    exit(1)

import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Test health check endpoint"""
    print("=" * 60)
    print("TEST 1: Health Check")
    print("=" * 60)
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        assert response.status_code == 200
        assert response.json()['status'] == 'active'
        print("\n✅ PASS - Health Check\n")
        return True
    except Exception as e:
        print(f"\n❌ FAIL - Health Check: {e}\n")
        return False

def test_info():
    """Test agent info endpoint"""
    print("=" * 60)
    print("TEST 2: Agent Info")
    print("=" * 60)
    
    try:
        response = requests.get(f"{BASE_URL}/info")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        assert response.status_code == 200
        data = response.json()
        assert 'capabilities' in data
        assert 'supported_sectors' in data
        print("\n✅ PASS - Agent Info\n")
        return True
    except Exception as e:
        print(f"\n❌ FAIL - Agent Info: {e}\n")
        return False

def test_technology_trend():
    """Test Technology sector trend analysis"""
    print("=" * 60)
    print("TEST 3: Technology Sector Analysis")
    print("=" * 60)
    
    payload = {
        "sector": "Technology",
        "keywords": ["AI", "automation", "cloud computing", "machine learning", "digital transformation"],
        "type": "emerging_trends"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        assert response.status_code == 200
        data = response.json()
        assert data['status'] == 'success'
        assert 'result' in data
        assert 'trend_direction' in data['result']
        print("\n✅ PASS - Technology Sector Analysis\n")
        return True
    except Exception as e:
        print(f"\n❌ FAIL - Technology Sector Analysis: {e}\n")
        return False

def test_ecommerce_trend():
    """Test E-commerce sector trend analysis"""
    print("=" * 60)
    print("TEST 4: E-commerce Sector Analysis")
    print("=" * 60)
    
    payload = {
        "sector": "E-commerce",
        "keywords": ["mobile shopping", "personalization", "social commerce", "quick delivery"],
        "type": "market_analysis"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        assert response.status_code == 200
        data = response.json()
        assert data['sector'] == 'E-commerce'
        print("\n✅ PASS - E-commerce Sector Analysis\n")
        return True
    except Exception as e:
        print(f"\n❌ FAIL - E-commerce Sector Analysis: {e}\n")
        return False

def test_healthcare_trend():
    """Test Healthcare sector trend analysis"""
    print("=" * 60)
    print("TEST 5: Healthcare Sector Analysis")
    print("=" * 60)
    
    payload = {
        "sector": "Healthcare",
        "keywords": ["telemedicine", "digital health", "AI diagnostics", "patient portals"],
        "type": "innovation_tracking"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        assert response.status_code == 200
        data = response.json()
        assert 'insights' in data['result']
        print("\n✅ PASS - Healthcare Sector Analysis\n")
        return True
    except Exception as e:
        print(f"\n❌ FAIL - Healthcare Sector Analysis: {e}\n")
        return False

def test_sustainability_trend():
    """Test Sustainability sector trend analysis"""
    print("=" * 60)
    print("TEST 6: Sustainability Sector Analysis")
    print("=" * 60)
    
    payload = {
        "sector": "Sustainability",
        "keywords": ["green business", "renewable energy", "carbon neutral", "ESG"],
        "type": "trend_forecast"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        assert response.status_code == 200
        data = response.json()
        assert 'recommendation' in data['result']
        print("\n✅ PASS - Sustainability Sector Analysis\n")
        return True
    except Exception as e:
        print(f"\n❌ FAIL - Sustainability Sector Analysis: {e}\n")
        return False

def main():
    """Run all tests"""
    print("\n")
    print("🚀" * 30)
    print("BUSINESS TREND MONITOR AGENT - INTEGRATION TESTS")
    print("Team: Abdul Hannan, Agha Ahsan, Minahil Asif")
    print("🚀" * 30)
    print("\n")
    
    tests = [
        test_health,
        test_info,
        test_technology_trend,
        test_ecommerce_trend,
        test_healthcare_trend,
        test_sustainability_trend
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    test_names = [
        "Health Check",
        "Agent Info",
        "Technology Sector Analysis",
        "E-commerce Sector Analysis",
        "Healthcare Sector Analysis",
        "Sustainability Sector Analysis"
    ]
    
    for name, result in zip(test_names, results):
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    passed = sum(results)
    total = len(results)
    success_rate = (passed / total) * 100
    
    print(f"\nTotal: {passed}/{total} tests passed")
    print(f"Success Rate: {success_rate:.1f}%")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print(f"\n⚠️ {total - passed} test(s) failed")

if __name__ == "__main__":
    main()
