# AI ERP System

## Overview
This project is a comprehensive AI-powered module designed to integrate with ERP systems in Manufacturing, Distribution, and Financial sectors. It provides intelligent features like predictive maintenance, route optimization, demand forecasting, and anomaly detection.

## Modules

### 1. Manufacturing
- **Predictive Maintenance:** Uses Random Forest to predict machine failure based on sensor data (Temperature, Vibration, Pressure, RPM).
- **Quality Control:** Uses a CNN (TensorFlow) to detect defects in product images.
- **Supply Chain Optimization:** Calculates Reorder Points and Safety Stock based on usage variability.

### 2. Distribution
- **Route Optimization:** Solves TSP (Traveling Salesman Problem) using Nearest Neighbor algorithm for delivery routes.
- **Demand Prediction:** Uses Exponential Smoothing (Holt-Winters) to forecast future product demand.
- **Inventory Management:** Performs ABC Analysis to categorize inventory importance.

### 3. Financial
- **Anomaly Detection:** Uses Isolation Forest to detect fraudulent or erroneous transactions.
- **Cash Flow Prediction:** Uses Linear Regression with lagged features to predict future cash flow.

## Project Structure
```
AI_ERP_System/
├── app/
│   ├── api/            # FastAPI Routers
│   ├── core/           # Config & Settings
│   ├── modules/        # AI Logic
│   │   ├── manufacturing/
│   │   ├── distribution/
│   │   └── financial/
├── data/               # Synthetic Data
├── models/             # Trained Model Artifacts (.joblib, .h5)
├── scripts/            # Training & Data Generation Scripts
├── docs/               # Detailed Documentation
├── requirements.txt
└── main.py
```

## Setup & Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate Data & Train Models**
   Before running the API, you must generate synthetic data and train the models.
   ```bash
   python scripts/generate_data_and_train.py
   ```
   This will create `.csv` files in `data/` and saved models in `models/`.

3. **Run the API**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access Documentation**
   Open `http://localhost:8000/docs` to see the interactive Swagger UI.

## Integration Guide
This system is designed as a microservice. Existing ERPs can consume these features via REST API calls.
- **Input:** JSON payload (or Image file for QC).
- **Output:** JSON response with predictions and probabilities.

## Technology Stack
- **Framework:** FastAPI
- **ML/AI:** Scikit-Learn, TensorFlow, OpenCV, Statsmodels
- **Data:** Pandas, NumPy
- **Server:** Uvicorn
