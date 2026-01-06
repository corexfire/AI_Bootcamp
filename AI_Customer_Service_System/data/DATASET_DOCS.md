# Dokumentasi Dataset AI Customer Service

## Ringkasan
Dataset ini `intents_large.json` dirancang untuk melatih model chatbot Customer Service dengan volume data yang besar (>1000 pola) dan variasi yang realistis, termasuk penanganan kesalahan pengetikan (typo).

## Statistik Dataset
- **Total Intents**: ~8 Kategori (Greeting, Order Status, Return, Cancel, Payment, Human Agent, dll)
- **Total Pola (Patterns)**: >1000 kalimat
- **Bahasa**: Inggris (en) dan Indonesia (id)
- **Typo Rate**: ~8% dari total data

## Struktur Data
Data disimpan dalam format JSON standar untuk pelatihan NLP:

```json
{
  "intents": [
    {
      "tag": "nama_intent",
      "patterns": {
        "en": ["List of English phrases..."],
        "id": ["Daftar frasa Indonesia..."]
      },
      "responses": {
        "en": ["English responses..."],
        "id": ["Respon Indonesia..."]
      },
      "context_set": ""
    }
  ]
}
```

### Penjelasan Field
- **tag**: Label kategori untuk klasifikasi intent (misal: `order_status`, `greeting`).
- **patterns**: Kumpulan kalimat input pengguna yang digunakan untuk melatih model.
  - **en**: Variasi dalam Bahasa Inggris.
  - **id**: Variasi dalam Bahasa Indonesia.
- **responses**: Jawaban yang diberikan bot jika intent terdeteksi.
- **context_set**: (Opsional) Digunakan untuk menyimpan state percakapan.

## Simulasi Typo
Dataset ini secara sengaja menyisipkan kesalahan pengetikan untuk meningkatkan ketahanan (robustness) model. Jenis typo yang disimulasikan:
1.  **Swap**: Menukar dua huruf bersebelahan (misal: "buka" -> "bkua")
2.  **Delete**: Menghapus satu huruf (misal: "makan" -> "mkan")
3.  **Double**: Menggandakan huruf (misal: "halo" -> "haloo")
4.  **Replace**: Mengganti huruf dengan huruf di dekatnya pada keyboard QWERTY (misal: "bisa" -> "bosa")

Contoh Data dengan Typo:
- "Dimana pkaet saya?" (Swap 'k' dan 'a')
- "Cancel oredr" (Swap 'r' dan 'e')
- "Halo minn" (Double 'n')

## Cara Menggunakan
Dataset ini siap digunakan oleh `nlp_engine.py` dalam proyek `AI_Customer_Service_System`.
Pastikan untuk mengarahkan script training ke file `data/intents_large.json`.

```python
# Contoh load dataset
with open('data/intents_large.json') as f:
    intents = json.load(f)
```
