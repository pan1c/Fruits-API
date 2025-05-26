# E2E test for the FastAPI application

import requests

BASE_URL = "http://api:8000"


def test_create_and_get():
    print("\n🧪 Creating a new fruit...")
    payload = {"fruit": "banana", "color": "yellow"}
    r = requests.post(f"{BASE_URL}/api/v1/fruits", json=payload)
    assert r.status_code == 201, f"Expected 201, got {r.status_code}"
    fruit = r.json()
    print(f"✅ Created fruit with ID: {fruit['id']}")
    assert fruit["id"] > 0

    print("📋 Fetching all fruits...")
    r = requests.get(f"{BASE_URL}/api/v1/fruits")
    fruits = r.json()
    assert any(f["fruit"] == "banana" for f in fruits), "Banana not found in fruit list"
    print("✅ Banana found in fruit list")

    print(f"🔍 Fetching fruit by ID {fruit['id']}...")
    r = requests.get(f"{BASE_URL}/api/v1/fruits/{fruit['id']}")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    assert (
        r.json()["color"] == "yellow"
    ), f"Expected color yellow, got {r.json()['color']}"
    print("✅ Color matches for banana")
