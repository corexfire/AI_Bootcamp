# Latihan Phase 4: Machine Learning Basic

## Soal 1: Konsep Dasar
Jelaskan perbedaan antara **Supervised Learning** dan **Unsupervised Learning**. Berikan masing-masing satu contoh kasus nyata!

## Soal 2: Train-Test Split
Mengapa kita perlu membagi data menjadi **Training Set** dan **Testing Set**? Apa yang terjadi jika kita menguji model menggunakan data yang sama dengan data training?

## Soal 3: Logistic Regression (Coding)
Gunakan dataset **Breast Cancer** dari Scikit-learn (`sklearn.datasets.load_breast_cancer`).
1. Load dataset.
2. Bagi data menjadi train (80%) dan test (20%).
3. Latih model **Logistic Regression**.
4. Tampilkan akurasi model pada data test.

## Soal 4: K-Means Clustering (Unsupervised)
Buatlah simulasi clustering sederhana menggunakan **K-Means**:
1. Generate data random 2D menggunakan `make_blobs` dari `sklearn.datasets`.
2. Lakukan clustering menjadi 3 cluster.
3. Tampilkan pusat cluster (centroid) yang ditemukan model.

## Soal 5: Evaluasi Model
Jika Anda memiliki model klasifikasi untuk mendeteksi penipuan kartu kredit (fraud detection), metrik mana yang lebih penting: **Accuracy** atau **Recall**? Jelaskan alasannya!
