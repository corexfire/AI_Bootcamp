import requests
import json

def solve_theory():
    print("--- Theory Answers ---")
    print("1. REST API: Standar arsitektur komunikasi web. GET: Mengambil data. POST: Mengirim data baru. POST dipakai untuk AI karena data input bisa besar/kompleks (JSON/Image) dan lebih aman daripada parameter URL.")
    print("2. Image: Blueprint/Template (Read-only). Container: Instance dari Image yang sedang berjalan (Runtime). Keuntungan: Konsistensi lingkungan (Works on my machine problem solved), isolasi, dan portabilitas.")
    print("3. Serialization: Mengubah objek memori (model) menjadi stream byte (file) agar bisa disimpan dan dimuat ulang nanti tanpa perlu training ulang.")
    print("5. Flask dev server single-threaded dan lambat. Untuk production, gunakan WSGI Server seperti Gunicorn atau uWSGI, dikombinasikan dengan Nginx sebagai reverse proxy dan Load Balancer.")

def solve_coding_challenge():
    print("\n--- Soal 4: Request Script ---")
    url = 'http://localhost:5000/predict'
    data = {"area": 50}
    
    print(f"Sending POST request to {url} with data {data}...")
    
    # Note: Ini akan error jika server tidak jalan. Kita wrap try-except.
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("Connection failed (Server not running):", e)

if __name__ == "__main__":
    solve_theory()
    solve_coding_challenge()
