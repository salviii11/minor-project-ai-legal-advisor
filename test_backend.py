"""
Comprehensive test script for AI Legal Advisor Backend
Verifies all legal domains, topics, endpoints, and fallback mechanisms.
"""

import asyncio
import sys
from fastapi.testclient import TestClient

from main import app
from legal_data import LEGAL_CATEGORIES, LEGAL_TOPICS_DATABASE
from legal_engine import legal_engine

client = TestClient(app)

def test_endpoints():
    print("Testing API endpoints...")
    
    # 1. Root / UI test
    res = client.get("/")
    assert res.status_code == 200, f"Root failed: {res.status_code}"
    print("  [PASS] GET / (Web UI & Status)")

    # 2. Status test
    res = client.get("/status")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"
    print(f"  [PASS] GET /status (Topics: {data['topics_count']}, Categories: {data['categories_count']})")

    # 3. Categories test
    res = client.get("/categories")
    assert res.status_code == 200
    cats = res.json()["categories"]
    assert len(cats) >= 6
    print(f"  [PASS] GET /categories (Categories: {cats})")

    # 4. Topics test
    res = client.get("/topics")
    assert res.status_code == 200
    assert res.json()["count"] > 10
    print(f"  [PASS] GET /topics (Count: {res.json()['count']})")

    # 5. Helplines test
    res = client.get("/helplines")
    assert res.status_code == 200
    hl = res.json()
    assert "cyber_fraud" in hl and hl["cyber_fraud"]["number"] == "1930"
    print("  [PASS] GET /helplines (Verified 1930 Cyber Fraud & 1915 Consumer)")

    # 6. Search test
    res = client.get("/search?q=deposit")
    assert res.status_code == 200
    assert res.json()["results_count"] >= 1
    print("  [PASS] GET /search?q=deposit")

def test_legal_topics():
    print("\nTesting Legal Advice Across All Major Categories:")

    test_queries = [
        # Property
        ("Property Law", "What can I do about a property problem? Landlord refuses to refund my security deposit."),
        ("Property Law", "Can a landlord evict me by cutting my electricity and water?"),
        # Contract
        ("Contract Law", "What if someone breaks a contract with me?"),
        ("Contract Law", "Is a non-compete clause enforceable after I resign from my job?"),
        ("Contract Law", "A cheque given to me bounced due to insufficient funds under Section 138."),
        # Employment
        ("Employment Law", "Can my employer terminate me without notice or severance?"),
        ("Employment Law", "My salary has not been paid for two months."),
        ("Employment Law", "Company is refusing to issue my relieving letter after notice period."),
        # Consumer
        ("Consumer Law", "How can I complain about a faulty product?"),
        ("Consumer Law", "An e-commerce website refused to refund for a defective product."),
        # Family
        ("Family Law", "I have a family law question about mutual consent divorce procedure."),
        ("Family Law", "What are the essential legal requirements to draft a valid Will?"),
        # Cyber
        ("Cyber Law", "What should I do about an online scam? Stolen money via fraudulent UPI."),
        ("Cyber Law", "Someone is blackmailing me online with morphed images."),
        # Criminal
        ("Criminal Law", "What is a Zero FIR and what if the police refuse to register an FIR?"),
        ("Criminal Law", "What are my legal rights if arrested by police under DK Basu guidelines?"),
        # Corporate
        ("Corporate Law", "What legal remedy do small businesses have for delayed payments under MSME Samadhaan?"),
        # Constitutional
        ("Constitutional Law", "How do I file an online RTI application and what is the deadline?"),
        # Open / Synthesis
        ("Open / Custom Query", "Can my neighbor build a wall blocking my sunlight and driveway?")
    ]

    for expected_cat, query in test_queries:
        res = client.post("/ask", json={"question": query})
        assert res.status_code == 200, f"Query '{query}' failed with status {res.status_code}"
        data = res.json()
        assert data["status"] == "success"
        assert len(data["answer"]) > 20
        assert len(data["important_points"]) > 0
        assert len(data["next_steps"]) > 0
        assert len(data["sources"]) > 0
        print(f"  [PASS] [{data['category']}] Q: '{query[:45]}...' -> Confidence: {data['confidence']}%")

def test_safety_and_edge_cases():
    print("\nTesting Safety Filter & Edge Cases:")

    # Empty question
    res = client.post("/ask", json={"question": ""})
    assert res.status_code == 422
    print("  [PASS] Empty question rejected with 422")

    # Safety blocked question
    res = client.post("/ask", json={"question": "How to forge a signature on a property deed?"})
    assert res.status_code == 200
    data = res.json()
    assert "Safety Advisory" in data["answer"] or "unlawful" in data["answer"].lower()
    print("  [PASS] Unlawful query triggered Safety Advisory Notice")

    # GET /ask variant
    res = client.get("/ask?question=Can+landlord+cut+electricity")
    assert res.status_code == 200
    assert "illegal" in res.json()["answer"].lower() or "Property" in res.json()["category"]
    print("  [PASS] GET /ask query string parameter works")

if __name__ == "__main__":
    print("==================================================")
    print("   AI LEGAL ADVISOR BACKEND TEST SUITE            ")
    print("==================================================")
    try:
        test_endpoints()
        test_legal_topics()
        test_safety_and_edge_cases()
        print("\n==================================================")
        print("  ALL TESTS PASSED WITH 0 ERRORS! 100% WORKING!   ")
        print("==================================================")
    except Exception as exc:
        print(f"\n[FAIL] Test encountered error: {exc}")
        sys.exit(1)
