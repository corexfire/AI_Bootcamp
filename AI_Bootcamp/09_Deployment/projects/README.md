# AI API Deployment with Docker

Project ini mendemonstrasikan cara membungkus aplikasi Flask AI (Prediction API) ke dalam Docker Container.

## Struktur File
- `app.py`: Aplikasi Flask utama yang memuat model ML.
- `Dockerfile`: Instruksi untuk membangun image Docker.
- `requirements.txt`: Daftar library Python yang dibutuhkan.

## Cara Build & Run (Lokal)
1. **Build Image**:
   ```bash
   docker build -t ai-prediction-api .
   ```
2. **Run Container**:
   ```bash
   docker run -p 5000:5000 ai-prediction-api
   ```

## Testing API
Kirim POST request ke `http://localhost:5000/predict`:
```json
{
    "area": 120
}
```
Response:
```json
{
    "currency": "Million IDR",
    "input_area": 120.0,
    "predicted_price": 240.0
}
```
