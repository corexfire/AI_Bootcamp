import pandas as pd
import numpy as np

def main():
    print("=== Pandas Data Analysis ===\n")

    # 1. Creating DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['Jakarta', 'Bandung', 'Jakarta', 'Surabaya', 'Bandung'],
        'Salary': [5000, 6000, 4500, 8000, 6500]
    }
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)

    # 2. Inspecting Data
    print("\n--- Info & Describe ---")
    print(df.info())
    print(df.describe())

    # 3. Filtering & Selection
    print("\n--- Filtering (Age > 25) ---")
    filtered_df = df[df['Age'] > 25]
    print(filtered_df)

    print("\n--- Selection (Name & Salary) ---")
    print(df[['Name', 'Salary']])

    # 4. GroupBy
    print("\n--- GroupBy City (Average Salary) ---")
    avg_salary_city = df.groupby('City')['Salary'].mean()
    print(avg_salary_city)

    # 5. Adding New Column
    print("\n--- Feature Engineering (Tax 10%) ---")
    df['Tax'] = df['Salary'] * 0.1
    print(df)

if __name__ == "__main__":
    main()
