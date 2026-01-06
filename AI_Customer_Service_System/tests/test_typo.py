import requests
import uuid
import time

BASE_URL = "http://localhost:8000/api/v1"

def test_typo_handling():
    print("\n=== Testing Typo Handling ===")
    session_id = str(uuid.uuid4())
    
    # Daftar kalimat dengan typo (Bahasa Inggris & Indonesia)
    typo_scenarios = [
        # English Typos
        {"msg": "Helo there", "expected": "greeting", "lang": "en"},  # Typo: Hello -> Helo
        {"msg": "Were is my ordr?", "expected": "check_order_status", "lang": "en"}, # Typo: Where -> Were, order -> ordr
        {"msg": "I wnt to talk to hman", "expected": "human_agent", "lang": "en"}, # Typo: want -> wnt, human -> hman
        
        # Indonesian Typos
        {"msg": "Halo min", "expected": "greeting", "lang": "id"},
        {"msg": "Dimna pket saya?", "expected": "check_order_status", "lang": "id"}, # Typo: Dimana -> Dimna, paket -> pket
        {"msg": "Sya mau kmplain", "expected": "complaint_product", "lang": "id"}, # Typo: Saya -> Sya, komplain -> kmplain
        {"msg": "Trims ya", "expected": "thanks", "lang": "id"}, # Slang: Terima kasih -> Trims
    ]
    
    for case in typo_scenarios:
        msg = case["msg"]
        lang = case["lang"]
        print(f"\nUser ({lang}) [Typo]: {msg}")
        
        try:
            response = requests.post(f"{BASE_URL}/chat", json={
                "session_id": session_id,
                "message": msg,
                "language": lang
            })
            if response.status_code == 200:
                data = response.json()
                detected_intent = data['intent']
                confidence = data['confidence']
                
                print(f"Bot Response: {data['response']}")
                print(f"Detected Intent: {detected_intent} (Confidence: {confidence:.2f})")
                
                if detected_intent == case["expected"]:
                    print("✅ Typo Handled Correctly")
                else:
                    print(f"❌ Failed. Expected {case['expected']}")
            else:
                print("Error:", response.text)
        except Exception as e:
            print("Connection failed:", e)

if __name__ == "__main__":
    print("Triggering Retraining first to apply new Char N-Grams model...")
    try:
        requests.post(f"{BASE_URL}/train")
        print("Training triggered. Waiting 2 seconds...")
        time.sleep(2)
    except:
        print("Could not trigger training via API. Assuming server will auto-reload or model is updated.")

    test_typo_handling()
