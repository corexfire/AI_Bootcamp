# Simple Movie Recommender System

Project ini adalah implementasi **Content-Based Filtering** sederhana untuk merekomendasikan film berdasarkan kemiripan **Genre**.

## Konsep
Menggunakan **TF-IDF Vectorizer** untuk mengubah teks genre menjadi vektor angka, kemudian menghitung **Cosine Similarity** antar film untuk menemukan film yang paling mirip.

## Dataset
`movies.csv` berisi daftar film beserta genrenya (Dummy subset dari MovieLens dataset).

## Cara Menjalankan
```bash
python main.py
```

## Contoh Output
Jika input adalah "Toy Story" (Animation/Children), sistem akan merekomendasikan film lain dengan genre serupa seperti "Balto" atau "Jumanji".
