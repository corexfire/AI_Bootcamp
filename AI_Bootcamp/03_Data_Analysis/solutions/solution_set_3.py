import pandas as pd
import matplotlib.pyplot as plt
import io

# Dummy CSV Data as String for demo
csv_data = """Name,Dept,Salary
John,IT,6000
Jane,HR,5000
Bob,IT,7000
Alice,HR,5500
Mike,Sales,4500"""

def solve_data_analysis():
    # Soal 1
    print("--- Soal 1 ---")
    df = pd.read_csv(io.StringIO(csv_data))
    print(df.head())
    print(f"Rata-rata Gaji: {df['Salary'].mean()}")
    
    # Soal 2
    print("\n--- Soal 2 ---")
    it_employees = df[df['Dept'] == 'IT']
    high_salary = df[df['Salary'] > 5500]
    print("IT Employees:\n", it_employees)
    print("Salary > 5500:\n", high_salary)
    
    # Soal 3
    print("\n--- Soal 3 ---")
    dept_salary = df.groupby('Dept')['Salary'].mean()
    print(dept_salary)
    
    # Soal 4
    print("\n--- Soal 4 ---")
    dept_counts = df['Dept'].value_counts()
    print(dept_counts)
    
    # Plotting (akan error jika tidak ada display, jadi kita print saja kodenya)
    # dept_counts.plot(kind='bar')
    # plt.title('Employee Count per Dept')
    # plt.show()
    print("Visualisasi code included in comments.")

if __name__ == "__main__":
    solve_data_analysis()
