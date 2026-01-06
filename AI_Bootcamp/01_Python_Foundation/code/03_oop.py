# 03_oop.py - Object Oriented Programming
# Materi: Class, Object, Inheritance

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []
        
    def add_score(self, score):
        """Menambahkan nilai ke daftar nilai siswa"""
        self.scores.append(score)
        print(f"Nilai {score} ditambahkan untuk {self.name}")
        
    def get_average(self):
        """Menghitung rata-rata nilai siswa"""
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
    
    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name}")

class AIStudent(Student):
    """Inheritance: AIStudent adalah tipe khusus dari Student"""
    def __init__(self, name, student_id, specialization):
        super().__init__(name, student_id) # Memanggil constructor parent
        self.specialization = specialization
        
    def display_info(self):
        # Overriding method parent
        super().display_info()
        print(f"Specialization: {self.specialization}")

def main():
    print("=== Demo OOP ===")
    
    # Membuat object
    student1 = AIStudent("Budi", "AI001", "Computer Vision")
    student1.add_score(85)
    student1.add_score(90)
    
    student1.display_info()
    print(f"Rata-rata nilai: {student1.get_average()}")

if __name__ == "__main__":
    main()
