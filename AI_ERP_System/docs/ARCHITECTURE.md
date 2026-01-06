# System Architecture

## Design Philosophy
The AI ERP System is designed as a **Microservice** that exposes AI capabilities via a RESTful API. This ensures loose coupling with the main ERP system (which could be SAP, Odoo, Microsoft Dynamics, or a custom solution).

## Data Pipeline

### 1. Data Ingestion
- **Training Phase:** Data is extracted from the ERP database (simulated here via CSV generation) and fed into the training scripts.
- **Inference Phase:** Real-time data is sent via HTTP POST requests to the API endpoints.

### 2. Preprocessing
Each module handles its own preprocessing:
- **Manufacturing:** Normalization of sensor data.
- **CV:** Resizing and normalization of images (128x128).
- **Financial:** Feature engineering (Lag creation, Date extraction).

### 3. Model Serving
- **FastAPI** handles the request lifecycle.
- **Singleton Pattern:** Models are loaded into memory once (lazy loading) to ensure low latency during inference.

## Integration Flow

### Example: Predictive Maintenance
1. **IoT Sensors** on factory machines send data to the Main ERP.
2. **Main ERP** aggregates data (e.g., 5-minute average).
3. **Main ERP** sends a POST request to `http://ai-erp/api/v1/manufacturing/predict-failure` with payload:
   ```json
   {
     "temperature": 85.5,
     "vibration": 0.4,
     "pressure": 105,
     "rpm": 1450,
     "usage_hours": 5000
   }
   ```
4. **AI System** returns:
   ```json
   {
     "prediction": 0,
     "failure_probability": 0.15,
     "status": "Healthy"
   }
   ```
5. **Main ERP** triggers a maintenance ticket if `status` is "Maintenance Required".

## Scalability
- The stateless nature of the API allows for horizontal scaling using Docker/Kubernetes.
- Models can be versioned and hot-swapped by updating the files in `models/` directory.

## Security
- API is protected via CORS settings.
- Future improvements: Add API Key authentication or OAuth2 in `app/core/security.py`.
