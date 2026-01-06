# Latihan Phase 9: Deployment

## Soal 1: REST API Concept
Apa itu **REST API**? Apa fungsi dari method HTTP **GET** dan **POST**? Mengapa kita biasanya menggunakan POST untuk mengirim data input ke model AI?

## Soal 2: Docker Basics
Jelaskan perbedaan antara **Docker Image** dan **Docker Container**! Apa keuntungan menggunakan Docker untuk deployment aplikasi AI?

## Soal 3: Serialization
Apa itu **Model Serialization** (Pickling/Joblib)? Mengapa kita perlu menyimpan model yang sudah dilatih ke dalam file?

## Soal 4: Coding - Simple Flask Request
Buatlah script Python menggunakan library `requests` untuk mengirim data ke API Flask yang sudah kita buat.
Input: `{"area": 50}`
URL: `http://localhost:5000/predict`
Tampilkan hasil JSON response-nya.

## Soal 5: Scalability
Jika API AI kita menerima 10.000 request per detik, apa yang akan terjadi jika kita hanya menggunakan `app.run()` bawaan Flask? Teknologi apa yang sebaiknya digunakan untuk production server (WSGI)?
