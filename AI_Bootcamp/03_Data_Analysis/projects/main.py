import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class SalesAnalyzer:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load_data(self):
        if not os.path.exists(self.data_path):
            print("File not found.")
            return
        self.df = pd.read_csv(self.data_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Total_Sales'] = self.df['Price'] * self.df['Quantity']
        print("Data loaded successfully.")
        print(self.df.head())

    def analyze_category_performance(self):
        print("\n--- Category Performance ---")
        category_sales = self.df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
        print(category_sales)
        return category_sales

    def analyze_daily_sales(self):
        print("\n--- Daily Sales ---")
        daily_sales = self.df.groupby('Date')['Total_Sales'].sum()
        print(daily_sales)
        return daily_sales

    def visualize_results(self):
        if self.df is None: return

        # Set style
        sns.set(style="whitegrid")
        
        # 1. Bar Chart: Category Sales
        category_sales = self.analyze_category_performance()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=category_sales.index, y=category_sales.values, palette='Blues_d')
        plt.title('Total Sales by Category')
        plt.ylabel('Revenue ($)')
        plt.savefig('category_sales.png')
        print("Saved: category_sales.png")

        # 2. Line Chart: Daily Sales
        daily_sales = self.analyze_daily_sales()
        plt.figure(figsize=(10, 6))
        plt.plot(daily_sales.index, daily_sales.values, marker='o', color='coral')
        plt.title('Daily Sales Trend')
        plt.ylabel('Revenue ($)')
        plt.grid(True)
        plt.savefig('daily_sales.png')
        print("Saved: daily_sales.png")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data', 'transactions.csv')
    
    analyzer = SalesAnalyzer(data_path)
    analyzer.load_data()
    analyzer.visualize_results()

if __name__ == "__main__":
    main()
