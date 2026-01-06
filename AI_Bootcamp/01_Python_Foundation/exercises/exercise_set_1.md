# Latihan Phase 1: Python Foundation

Silakan kerjakan soal-soal berikut di file Python terpisah.

## Soal 1: Pengecekan Bilangan Prima
Buatlah sebuah fungsi `is_prime(n)` yang menerima input integer `n` dan mengembalikan `True` jika `n` adalah bilangan prima, dan `False` jika bukan.

Contoh:
```python
is_prime(7)  # Output: True
is_prime(10) # Output: False
```

## Soal 2: Class Persegi Panjang
Buatlah class `Rectangle` dengan spesifikasi:
- Memiliki atribut `length` (panjang) dan `width` (lebar).
- Memiliki method `area()` yang mengembalikan luas persegi panjang.
- Memiliki method `perimeter()` yang mengembalikan keliling persegi panjang.

Contoh:
```python
rect = Rectangle(10, 5)
print(rect.area())      # Output: 50
print(rect.perimeter()) # Output: 30
```

## Soal 3: Filter Angka Genap (List Comprehension)
Diberikan sebuah list angka: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
Gunakan **List Comprehension** untuk membuat list baru yang hanya berisi angka genap dari list tersebut.

Output yang diharapkan: `[2, 4, 6, 8, 10]`

## Soal 4: Hitung Kata
Buatlah fungsi `count_words(sentence)` yang menerima string kalimat dan mengembalikan dictionary yang berisi frekuensi kemunculan setiap kata (case-insensitive).

Contoh:
```python
text = "Ini adalah apel dan ini adalah jeruk"
print(count_words(text))
# Output: {'ini': 2, 'adalah': 2, 'apel': 1, 'dan': 1, 'jeruk': 1}
```

## Soal 5: Palindrome Checker
Buatlah fungsi `is_palindrome(text)` untuk mengecek apakah sebuah kata/kalimat adalah palindrom (dibaca sama dari depan dan belakang). Abaikan spasi dan besar kecil huruf.

Contoh:
```python
is_palindrome("Katak") # True
is_palindrome("Kasur Rusak") # True
is_palindrome("Hello") # False
```
