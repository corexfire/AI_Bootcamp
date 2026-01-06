# House Price Prediction

Project ini membangun model Machine Learning sederhana menggunakan **Linear Regression** untuk memprediksi harga rumah berdasarkan fitur-fitur properti.

## Dataset
Dataset dummy `housing.csv` memiliki fitur:
- `Area`: Luas tanah/bangunan (m2)
- `Bedrooms`: Jumlah kamar tidur
- `Age`: Umur bangunan (tahun)
- `Location_Score`: Skor lokasi (1-10)
- `Price`: Harga rumah (Target Variable)

## Tech Stack
- Python
- Scikit-learn (Modeling)
- Pandas (Data Processing)
- Matplotlib (Visualization)

## Cara Menjalankan
```bash
python main.py
```

## Hasil
Program akan menampilkan metrik evaluasi (MAE, RMSE, R2 Score) dan menyimpan grafik perbandingan harga asli vs prediksi (`prediction_plot.png`).
