from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load Model (Pastikan model sudah dilatih dan disimpan sebelumnya)
# Kita akan buat dummy model file jika belum ada untuk demo
MODEL_PATH = 'model.pkl'

if not os.path.exists(MODEL_PATH):
    # Create dummy model for demonstration
    from sklearn.linear_model import LinearRegression
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 4, 6, 8])
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print("Dummy model created.")

model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return """
    <h1>House Price Prediction API</h1>
    <p>Use /predict endpoint with POST request.</p>
    <p>Example JSON: {"area": 100}</p>
    """

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        area = float(data['area'])
        
        # Prediksi
        prediction = model.predict([[area]])[0]
        
        return jsonify({
            "input_area": area,
            "predicted_price": prediction,
            "currency": "Million IDR"
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    # Host 0.0.0.0 agar bisa diakses dari luar container
    app.run(host='0.0.0.0', port=5000)
