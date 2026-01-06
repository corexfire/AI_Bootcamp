import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def main():
    print("=== Data Visualization Demo ===\n")
    
    # Generate Dummy Data
    np.random.seed(42)
    days = list(range(1, 31))
    sales = np.random.randint(100, 500, size=30)
    
    df = pd.DataFrame({'Day': days, 'Sales': sales})
    
    # 1. Line Plot (Matplotlib)
    plt.figure(figsize=(10, 5))
    plt.plot(df['Day'], df['Sales'], marker='o', linestyle='-', color='b')
    plt.title("Daily Sales Trend")
    plt.xlabel("Day")
    plt.ylabel("Sales")
    plt.grid(True)
    # plt.show() # Uncomment to view
    print("Line plot created.")

    # 2. Histogram (Seaborn)
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Sales'], bins=10, kde=True, color='green')
    plt.title("Sales Distribution")
    # plt.show() # Uncomment to view
    print("Histogram created.")

    # 3. Bar Plot
    categories = ['Electronics', 'Clothing', 'Food', 'Books']
    values = [4500, 3200, 5800, 1200]
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=categories, y=values, palette='viridis')
    plt.title("Sales by Category")
    # plt.show() # Uncomment to view
    print("Bar plot created.")

if __name__ == "__main__":
    main()
