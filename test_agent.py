"""
Simple Integration Tests for Market Trend Monitor Agent

Team: Abdul Hannan (22i-2441), Agha Ahsan (22i-1117), Minahil Asif (22i-2710)

Note: Install requests first: pip install requests
"""

try:
    import requests
except ImportError:
    print("❌ Error: 'requests' module not installed")
    print("Please run: pip install requests")
    exit(1)

import json

BASE_URL = "http://localhost:5000"

def print_header(text):
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)

def test_health():
    """Test 1: Health Check"""
    print_header("TEST 1: Health Check")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_info():
    """Test 2: Agent Info"""
    print_header("TEST 2: Agent Info")
    try:
        response = requests.get(f"{BASE_URL}/info")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_trend_analysis():
    """Test 3: Trend Analysis"""
    print_header("TEST 3: Trend Analysis")
    try:
        payload = {
            "type": "trend",
            "market": "BTC/USD",
            "prices": [45000, 45500, 46000, 45800, 46500, 47000, 47500],
            "volumes": [1200000, 1300000, 1250000, 1400000, 1350000, 1450000, 1500000]
        }
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_sentiment_analysis():
    """Test 4: Sentiment Analysis"""
    print_header("TEST 4: Sentiment Analysis")
    try:
        payload = {
            "type": "sentiment",
            "market": "ETH/USD",
            "texts": [
                "Bitcoin shows strong bullish momentum",
                "Market rally continues with high growth",
                "Investors profit from surge in prices"
            ]
        }
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_price_prediction():
    """Test 5: Price Prediction"""
    print_header("TEST 5: Price Prediction")
    try:
        payload = {
            "type": "prediction",
            "market": "BTC/USD",
            "prices": [45000, 45200, 45500, 45800, 46000, 46300, 46500, 46800, 47000],
            "prediction_days": 7
        }
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_anomaly_detection():
    """Test 6: Anomaly Detection"""
    print_header("TEST 6: Anomaly Detection")
    try:
        payload = {
            "type": "anomaly",
            "market": "BTC/USD",
            "prices": [45000, 45500, 46000, 52000, 46500, 47000, 46800, 47200, 55000, 47500, 47300, 47600]
        }
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("\n" + "🚀" * 30)
    print("MARKET TREND MONITOR AGENT - INTEGRATION TESTS")
    print("Team: Abdul Hannan, Agha Ahsan, Minahil Asif")
    print("🚀" * 30)
    
    results = []
    
    # Run all tests
    results.append(("Health Check", test_health()))
    results.append(("Agent Info", test_info()))
    results.append(("Trend Analysis", test_trend_analysis()))
    results.append(("Sentiment Analysis", test_sentiment_analysis()))
    results.append(("Price Prediction", test_price_prediction()))
    results.append(("Anomaly Detection", test_anomaly_detection()))
    
    # Print summary
    print_header("TEST SUMMARY")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print("\n⚠️ Some tests failed. Make sure agent is running on port 5000.")

if __name__ == "__main__":
    main()
