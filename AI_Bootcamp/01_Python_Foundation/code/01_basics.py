# 01_basics.py - Pengenalan Python Dasar
# Materi: Syntax, Variables, Data Types, Control Flow

def main():
    print("=== Belajar Python Dasar ===")
    
    # 1. Variables & Data Types
    name = "Bootcamp AI"  # String
    batch = 10            # Integer
    is_active = True      # Boolean
    rating = 4.8          # Float
    
    print(f"Nama: {name}, Batch: {batch}, Rating: {rating}")
    
    # 2. List & Dictionary (Struktur Data Dasar)
    modules = ["Python", "Math", "ML", "DL"]
    student_score = {"Alice": 85, "Bob": 90, "Charlie": 78}
    
    print(f"Modul pertama: {modules[0]}")
    print(f"Nilai Bob: {student_score['Bob']}")
    
    # 3. Control Flow (If-Else)
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"
    
    print(f"Score {score} mendapat grade {grade}")
    
    # 4. Looping (For & While)
    print("\nDaftar Modul:")
    for module in modules:
        print(f"- {module}")
        
    print("\nCountdown:")
    count = 3
    while count > 0:
        print(count)
        count -= 1
    print("Start!")

if __name__ == "__main__":
    main()
