import csv
import os

class Student:
    def __init__(self, student_id, name, math, science, english):
        self.student_id = student_id
        self.name = name
        self.math = float(math)
        self.science = float(science)
        self.english = float(english)
        self.average = 0
        self.status = ""

    def calculate_average(self):
        self.average = (self.math + self.science + self.english) / 3

    def determine_status(self):
        # Kriteria lulus: Rata-rata >= 70
        if self.average >= 70:
            self.status = "LULUS"
        else:
            self.status = "TIDAK LULUS"

class GradeAnalyzer:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.students = []

    def load_data(self):
        if not os.path.exists(self.csv_file):
            print(f"Error: File {self.csv_file} tidak ditemukan.")
            return

        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    row['ID'], 
                    row['Name'], 
                    row['Math'], 
                    row['Science'], 
                    row['English']
                )
                self.students.append(student)
        print(f"Berhasil memuat {len(self.students)} data siswa.")

    def process_grades(self):
        for student in self.students:
            student.calculate_average()
            student.determine_status()

    def generate_report(self):
        print("\n=== Laporan Nilai Siswa ===")
        print(f"{'ID':<5} {'Nama':<10} {'Rata-rata':<10} {'Status':<10}")
        print("-" * 40)
        
        for student in self.students:
            print(f"{student.student_id:<5} {student.name:<10} {student.average:<10.2f} {student.status:<10}")
            
    def save_report(self, output_file):
        with open(output_file, 'w') as f:
            f.write("ID,Nama,Rata-rata,Status\n")
            for student in self.students:
                f.write(f"{student.student_id},{student.name},{student.average:.2f},{student.status}\n")
        print(f"\nLaporan tersimpan di {output_file}")

def main():
    # Path file relatif terhadap script ini
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data', 'students.csv')
    
    analyzer = GradeAnalyzer(data_path)
    analyzer.load_data()
    analyzer.process_grades()
    analyzer.generate_report()
    
    output_path = os.path.join(current_dir, 'report.txt')
    analyzer.save_report(output_path)

if __name__ == "__main__":
    main()
