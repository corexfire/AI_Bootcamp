# Jawaban Latihan Phase 1

def is_prime(n):
    """Soal 1: Pengecekan Bilangan Prima"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class Rectangle:
    """Soal 2: Class Persegi Panjang"""
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

def even_filter_example():
    """Soal 3: List Comprehension"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = [n for n in numbers if n % 2 == 0]
    return evens

def count_words(sentence):
    """Soal 4: Hitung Kata"""
    words = sentence.lower().split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def is_palindrome(text):
    """Soal 5: Palindrome Checker"""
    # Hapus spasi dan jadikan lowercase
    clean_text = "".join(text.lower().split())
    # Bandingkan dengan kebalikannya
    return clean_text == clean_text[::-1]

# Testing Solutions
if __name__ == "__main__":
    print("1. Prime Check (7):", is_prime(7))
    
    rect = Rectangle(10, 5)
    print(f"2. Rectangle Area: {rect.area()}, Perimeter: {rect.perimeter()}")
    
    print("3. Evens:", even_filter_example())
    
    text = "Ini adalah apel dan ini adalah jeruk"
    print("4. Word Count:", count_words(text))
    
    print("5. Palindrome 'Kasur Rusak':", is_palindrome("Kasur Rusak"))
