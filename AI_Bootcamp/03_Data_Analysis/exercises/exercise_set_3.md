# Latihan Phase 3: Data Analysis

## Soal 1: Load & Inspect
Diberikan file CSV (buatlah dummy csv sederhana `employees.csv`):
```csv
Name,Dept,Salary
John,IT,6000
Jane,HR,5000
Bob,IT,7000
Alice,HR,5500
Mike,Sales,4500
```
1. Load CSV ke DataFrame.
2. Tampilkan 5 baris pertama.
3. Tampilkan rata-rata Gaji (Salary).

## Soal 2: Filtering
Dari DataFrame di atas:
1. Filter karyawan yang bekerja di departemen 'IT'.
2. Filter karyawan dengan gaji di atas 5500.

## Soal 3: Grouping
Hitung rata-rata gaji untuk setiap Departemen.
Output yang diharapkan:
```
Dept
HR       5250.0
IT       6500.0
Sales    4500.0
```

## Soal 4: Visualisasi Sederhana
Buatlah Bar Chart sederhana yang menampilkan jumlah karyawan di setiap departemen menggunakan `value_counts()` dan Matplotlib.
