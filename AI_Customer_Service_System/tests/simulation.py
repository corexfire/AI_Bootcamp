import requests
import uuid
import time

BASE_URL = "http://localhost:8000/api/v1"

def test_chat_flow_english():
    print("\n=== Testing Chat Flow (English) ===")
    session_id = str(uuid.uuid4())
    
    scenarios = [
        "Hello",
        "Where is my order?",
        "ORD-12345", 
        "Bye"
    ]
    
    for msg in scenarios:
        print(f"\nUser: {msg}")
        try:
            response = requests.post(f"{BASE_URL}/chat", json={
                "session_id": session_id,
                "message": msg,
                "language": "en"
            })
            if response.status_code == 200:
                data = response.json()
                print(f"Bot: {data['response']}")
            else:
                print("Error:", response.text)
        except Exception as e:
            print("Connection failed:", e)

def test_chat_flow_indonesian():
    print("\n=== Testing Chat Flow (Indonesian) ===")
    session_id = str(uuid.uuid4())
    
    scenarios = [
        "Halo",
        "Dimana pesanan saya?",
        "ORD-12345", 
        "Terima kasih",
        "Dah"
    ]
    
    for msg in scenarios:
        print(f"\nUser: {msg}")
        try:
            response = requests.post(f"{BASE_URL}/chat", json={
                "session_id": session_id,
                "message": msg,
                "language": "id"
            })
            if response.status_code == 200:
                data = response.json()
                print(f"Bot: {data['response']}")
            else:
                print("Error:", response.text)
        except Exception as e:
            print("Connection failed:", e)

if __name__ == "__main__":
    print("Make sure uvicorn server is running on port 8000!")
    print("Wait for server reload if you just updated code...")
    time.sleep(2) 
    
    test_chat_flow_english()
    test_chat_flow_indonesian()
