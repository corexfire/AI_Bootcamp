# Simple Motion Detector (CCTV Style)

Project ini menggunakan **OpenCV** untuk mendeteksi gerakan dalam video feed dari webcam.

## Cara Kerja
1. Menggunakan algoritma **Background Subtraction (MOG2)** untuk memisahkan objek bergerak dari latar belakang statis.
2. Melakukan operasi morfologi (Erosion/Dilation) untuk menghilangkan noise.
3. Mencari kontur (contours) pada mask hasil pengurangan background.
4. Jika kontur cukup besar (area > 500), dianggap sebagai gerakan dan digambar kotak merah.

## Requirements
- opencv-python
- numpy

## Cara Menjalankan
```bash
python main.py
```
Aplikasi akan membuka webcam. Jika ada gerakan, status akan berubah menjadi "Motion Detected!" dan objek akan ditandai kotak merah. Tekan 'q' untuk keluar.
