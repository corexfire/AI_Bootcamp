# Panduan Pelatihan dan Pengembangan AI Chatbot

Dokumen ini menjelaskan cara menggunakan, melatih, dan menambahkan pengetahuan baru ke dalam sistem AI Customer Service.

## 1. Konsep Dasar "Belajar"
AI Chatbot ini menggunakan pendekatan **Supervised Learning** (Pembelajaran Terawasi). Artinya, AI tidak belajar sendiri secara ajaib dari percakapan pengguna secara langsung (untuk mencegah respons yang ngawur), melainkan **belajar dari data latih** yang kita sediakan.

Setiap kali Anda ingin AI "pintar" dalam topik baru, Anda harus:
1. Menambahkan contoh pertanyaan (Pattern) dan jawaban (Response) ke dalam database pengetahuannya (`intents.json`).
2. Melakukan proses **Training Ulang** (Retraining) agar model matematika-nya diperbarui.

---

## 2. Cara Menambahkan Pengetahuan Baru

Semua pengetahuan bot disimpan di file:
`AI_Customer_Service_System/data/intents.json`

Format data adalah JSON. Untuk menambah topik baru, tambahkan objek baru ke dalam list `"intents"`.

### Contoh: Menambah Topik "Cara Ganti Password"

Buka `data/intents.json` dan tambahkan blok berikut:

```json
{
  "tag": "reset_password",
  "patterns": {
    "en": ["How do I reset my password?", "Change password", "Forgot login"],
    "id": ["Gimana cara ganti password?", "Lupa sandi", "Reset password dong"]
  },
  "responses": {
    "en": ["You can reset your password by clicking 'Forgot Password' on the login page."],
    "id": ["Anda bisa mereset kata sandi dengan mengklik 'Lupa Password' di halaman login."]
  },
  "context_set": ""
}
```

**Tips:**
- `tag`: Nama unik untuk topik tersebut (gunakan huruf kecil dan underscore).
- `patterns`: Variasi kalimat yang mungkin diucapkan user. Semakin banyak variasi, semakin pintar AI-nya.
- `responses`: Jawaban yang akan diberikan bot.

---

## 3. Cara Melatih Ulang Model (Training)

Setelah mengubah `intents.json`, Anda **WAJIB** melatih ulang model agar perubahan tersebut dikenali. Ada 2 cara untuk melakukannya:

### Cara A: Restart Server (Otomatis)
Secara default, setiap kali server dimatikan dan dinyalakan ulang, sistem akan otomatis melatih ulang model jika file model belum ada atau ingin di-refresh.

Namun, untuk memaksa training saat server sedang berjalan (tanpa restart), gunakan Cara B atau C.

### Cara B: Via API (Tanpa Restart Server)
Kami telah menyediakan endpoint khusus untuk memicu training ulang.
Kirim request **POST** ke endpoint `/api/v1/train`.

**Contoh menggunakan cURL:**
```bash
curl -X POST http://localhost:8000/api/v1/train
```

**Response:**
```json
{
  "message": "Model retrained successfully",
  "total_intents": 15
}
```

### Cara C: Via Script Manual (CLI)
Anda bisa menjalankan script Python khusus untuk training:

```bash
python scripts/train_model.py
```

---

## 4. Mekanisme "Belajar Sendiri" (Active Learning - Lanjutan)

Jika Anda ingin sistem menjadi lebih pintar berdasarkan percakapan nyata yang terjadi (semi-otomatis), Anda bisa menerapkan alur kerja berikut:

1. **Analisis Log**: Buka Dashboard Analytics atau cek database. Lihat pesan-pesan yang masuk ke intent `fallback` (artinya bot tidak mengerti).
2. **Review Manual**: Tim manusia melihat pertanyaan apa yang gagal dijawab.
3. **Update Intents**: Masukkan pertanyaan-pertanyaan tersebut ke dalam `intents.json` di tag yang sesuai, atau buat tag baru.
4. **Retrain**: Lakukan training ulang.

Dengan siklus ini, AI akan terus belajar dari kasus nyata di lapangan.

---

## Ringkasan Workflow
1. **Edit** `data/intents.json` -> Tambah intent baru.
2. **Simpan** file.
3. **Trigger Training** (via API atau Script).
4. **Test** bot dengan pertanyaan baru.
