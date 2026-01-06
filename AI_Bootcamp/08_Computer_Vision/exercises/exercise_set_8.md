# Latihan Phase 8: Computer Vision

## Soal 1: Image Representation
Bagaimana sebuah gambar berwarna (RGB) direpresentasikan dalam komputer? Berapa dimensi array-nya jika gambar berukuran 100x100 pixel?

## Soal 2: Grayscale
Mengapa dalam banyak algoritma Computer Vision (seperti Face Detection), kita perlu mengubah gambar menjadi **Grayscale** (hitam putih) terlebih dahulu?

## Soal 3: Thresholding
Jelaskan apa itu **Image Thresholding**! Apa bedanya Simple Thresholding dengan Adaptive Thresholding?

## Soal 4: Coding - Color Detection
Buatlah script OpenCV sederhana yang bisa mendeteksi objek berwarna **BIRU** saja dari webcam/gambar.
Hint:
1. Convert BGR ke HSV color space.
2. Tentukan range warna biru (Lower & Upper HSV).
3. Gunakan `cv2.inRange` untuk membuat mask.
4. Tampilkan hasil mask.

## Soal 5: Edge Detection
Apa fungsi dari **Canny Edge Detection**? Parameter apa yang paling berpengaruh dalam menentukan mana garis tepi yang kuat dan mana yang lemah?
