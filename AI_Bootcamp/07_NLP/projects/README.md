# Simple AI Chatbot

Project ini adalah implementasi Chatbot sederhana berbasis **Intent Classification**.
Chatbot dilatih untuk mengenali maksud (intent) pengguna dari teks input dan memberikan respons yang sesuai.

## Cara Kerja
1. **Dataset**: File `data/intents.json` berisi pola kalimat (patterns) dan label intent (tag).
2. **NLP**: Menggunakan **CountVectorizer** (Bag of Words) untuk mengubah teks menjadi angka.
3. **Model**: Menggunakan **MLPClassifier** (Multi-Layer Perceptron) dari Scikit-learn untuk klasifikasi intent.
4. **Response**: Memilih respons acak berdasarkan intent yang terdeteksi.

## Cara Menjalankan
```bash
python main.py
```
Ketik pesan Anda di terminal, misalnya "Hello", "What do you sell?", atau "Bye".

## Dependencies
- scikit-learn
- nltk
- numpy
