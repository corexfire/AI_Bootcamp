# Statistical Calculator Project

Project ini mendemonstrasikan penggunaan NumPy untuk melakukan analisis statistik deskriptif pada dataset penjualan.

## Fitur
- Load data numerik dari CSV menggunakan NumPy.
- Menghitung Mean, Median, Standard Deviation, Min, Max.
- Menghitung Z-Score (Normalisasi) untuk setiap data point.
- Mengenerate dummy data secara otomatis jika file tidak ditemukan.

## Requirements
- Python 3.x
- NumPy (`pip install numpy`)

## Cara Menjalankan
```bash
python main.py
```

## Penjelasan Matematis
- **Mean**: Rata-rata aritmatika.
- **Median**: Nilai tengah data yang sudah diurutkan.
- **Std Dev**: Ukuran sebaran data terhadap rata-ratanya.
- **Z-Score**: `(x - mean) / std_dev`. Menunjukkan berapa standar deviasi suatu data point dari rata-ratanya.
