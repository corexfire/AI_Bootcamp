import cv2
import numpy as np

def solve_theory():
    print("--- Theory Answers ---")
    print("1. Gambar RGB direpresentasikan sebagai 3D Array (Height, Width, Channels). Untuk 100x100 pixel, dimensinya adalah (100, 100, 3).")
    print("2. Grayscale mengurangi kompleksitas komputasi (dari 3 channel jadi 1 channel) dan fokus pada intensitas cahaya/struktur objek, bukan warna.")
    print("3. Thresholding mengubah gambar grayscale menjadi biner (hitam putih mutlak) berdasarkan batas nilai pixel tertentu. Adaptive thresholding menghitung batas secara lokal untuk area gambar yang berbeda (bagus untuk pencahayaan tidak rata).")
    print("5. Canny Edge Detection mendeteksi tepi objek dengan mencari perubahan intensitas pixel yang drastis (gradient). Parameter penting: Threshold1 (batas bawah) dan Threshold2 (batas atas) untuk hysteresis.")

def solve_coding_challenge():
    print("\n--- Soal 4: Blue Color Detection (Simulation) ---")
    # Kita buat dummy image biru karena tidak bisa akses webcam di environment ini
    img = np.zeros((300, 300, 3), dtype='uint8')
    cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), -1) # Kotak Biru (BGR format)
    cv2.rectangle(img, (200, 50), (250, 100), (0, 0, 255), -1) # Kotak Merah
    
    # 1. Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 2. Define Range of Blue Color in HSV
    # Blue in HSV is around 120. Range: [110, 50, 50] to [130, 255, 255]
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # 3. Create Mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # 4. Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask=mask)
    
    print("Blue detection mask created. (Code runs successfully)")
    # cv2.imshow('Mask', mask); cv2.imshow('Result', res); cv2.waitKey(0)

if __name__ == "__main__":
    solve_theory()
    solve_coding_challenge()
