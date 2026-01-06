from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Dummy Model Load (Simulation)
# Dalam production, kita load model pickle/h5 di sini
print("Loading AI Model...")

@app.route('/')
def home():
    return "AI API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Menerima data JSON
        data = request.get_json()
        
        # Contoh input: {"features": [5.1, 3.5, 1.4, 0.2]}
        features = np.array(data['features'])
        
        # Dummy Prediction Logic (Misal Iris Classification)
        # 0: Setosa, 1: Versicolor, 2: Virginica
        # Anggap model melakukan prediksi
        prediction = np.argmax(features) % 3 # Random logic for demo
        classes = ['Setosa', 'Versicolor', 'Virginica']
        
        result = {
            "prediction": int(prediction),
            "class_name": classes[prediction],
            "status": "success"
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
