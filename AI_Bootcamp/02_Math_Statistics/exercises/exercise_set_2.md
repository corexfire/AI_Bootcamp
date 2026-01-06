# Latihan Phase 2: Matematika & Statistik

## Soal 1: Operasi Matrix
Diketahui Matrix A dan B sebagai berikut:
```python
A = [[2, 4], [1, 3]]
B = [[5, 1], [2, 6]]
```
Hitunglah:
1. Penjumlahan A + B
2. Perkalian A x B (Dot Product)
3. Transpose dari hasil perkalian tersebut.

## Soal 2: Analisis Tinggi Badan
Diberikan list tinggi badan siswa (cm): `[165, 170, 155, 162, 180, 175, 168, 158]`.
Gunakan NumPy untuk menghitung:
1. Rata-rata tinggi badan.
2. Standar deviasi.
3. Siapa saja yang tingginya di atas rata-rata?

## Soal 3: Normalisasi Min-Max
Buatlah fungsi `min_max_scaling(data)` yang menerima array NumPy dan mengubah nilainya menjadi rentang 0 sampai 1 menggunakan rumus:
`x_scaled = (x - min) / (max - min)`

## Soal 4: Jarak Euclidean
Buatlah fungsi untuk menghitung jarak Euclidean antara dua titik vector 2D, misal titik P(1, 2) dan Q(4, 6).
Rumus: `sqrt((x2-x1)^2 + (y2-y1)^2)`
Gunakan fungsi `np.sqrt` dan operasi vector.
