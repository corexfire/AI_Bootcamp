# 02_functions.py - Fungsi dan Modular Programming
# Materi: Function, Parameters, Return Values

def calculate_average(numbers):
    """
    Menghitung rata-rata dari list angka.
    Args:
        numbers (list): List berisi angka (int/float)
    Returns:
        float: Rata-rata nilai
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def classify_grade(average):
    """
    Mengklasifikasikan nilai rata-rata ke dalam grade.
    """
    if average >= 85:
        return "High Distinction"
    elif average >= 75:
        return "Distinction"
    elif average >= 65:
        return "Credit"
    else:
        return "Pass"

def main():
    print("=== Demo Fungsi ===")
    scores = [80, 85, 90, 75, 88]
    
    avg = calculate_average(scores)
    grade = classify_grade(avg)
    
    print(f"Nilai: {scores}")
    print(f"Rata-rata: {avg}")
    print(f"Klasifikasi: {grade}")

if __name__ == "__main__":
    main()
