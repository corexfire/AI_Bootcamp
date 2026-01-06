import sys
import os

# Tambahkan root project ke path agar bisa import modul app
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.core.nlp_engine import nlp_engine

def train():
    print("=== Manual Training Started ===")
    try:
        nlp_engine.load_data() # Reload JSON data
        nlp_engine.train()     # Retrain model
        print("\n[SUCCESS] Model has been retrained and saved to data/model.pkl")
    except Exception as e:
        print(f"\n[ERROR] Training failed: {e}")

if __name__ == "__main__":
    train()
