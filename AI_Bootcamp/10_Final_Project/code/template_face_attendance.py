# Face Attendance System (Template)

import cv2
import os
from datetime import datetime

# Path untuk menyimpan foto wajah terdaftar
DB_PATH = "face_db"

def create_db():
    if not os.path.exists(DB_PATH):
        os.makedirs(DB_PATH)
        print("Database folder created.")

def register_user(name):
    cap = cv2.VideoCapture(0)
    print(f"Registrasi: {name}. Tatap kamera...")
    
    while True:
        ret, frame = cap.read()
        cv2.imshow("Register Face (Press 's' to save)", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_name = os.path.join(DB_PATH, f"{name}.jpg")
            cv2.imwrite(img_name, frame)
            print(f"User {name} registered successfully!")
            break
            
    cap.release()
    cv2.destroyAllWindows()

def start_attendance():
    # Ini adalah template logika sederhana
    # Untuk implementasi penuh, gunakan library 'face_recognition' untuk membandingkan encoding wajah
    print("Memulai sistem absensi... (Logika pengenalan wajah perlu diimplementasikan)")
    
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        
        # Placeholder deteksi wajah OpenCV
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
            
        cv2.imshow("Attendance System", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

def main():
    create_db()
    print("=== Face Attendance System ===")
    print("1. Register User")
    print("2. Start Attendance")
    choice = input("Pilih menu: ")
    
    if choice == '1':
        name = input("Masukkan Nama: ")
        register_user(name)
    elif choice == '2':
        start_attendance()
    else:
        print("Invalid menu")

if __name__ == "__main__":
    main()
