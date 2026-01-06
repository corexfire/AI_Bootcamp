import numpy as np
import os

class StatsCalculator:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None
        self.results = {}

    def load_data(self):
        """Memuat data numerik dari file teks/csv (single column)"""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"File {self.data_path} not found")
        
        # Load data using numpy, skipping header if present
        try:
            self.data = np.loadtxt(self.data_path, skiprows=1, delimiter=',')
            print(f"Data loaded: {len(self.data)} samples")
        except Exception as e:
            print(f"Error loading data: {e}")

    def analyze(self):
        if self.data is None:
            print("No data to analyze.")
            return

        self.results['mean'] = np.mean(self.data)
        self.results['median'] = np.median(self.data)
        self.results['std_dev'] = np.std(self.data)
        self.results['min'] = np.min(self.data)
        self.results['max'] = np.max(self.data)
        
        # Normalization (Z-Score)
        self.results['z_scores'] = (self.data - self.results['mean']) / self.results['std_dev']

    def print_report(self):
        print("\n=== Statistical Analysis Report ===")
        for key, value in self.results.items():
            if key != 'z_scores':
                print(f"{key.capitalize()}: {value:.4f}")
        
        print("\nFirst 5 Normalized Data (Z-Scores):")
        print(self.results['z_scores'][:5])

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(current_dir, 'data', 'sales_data.csv')
    
    # Create dummy data if not exists (for demo purpose)
    if not os.path.exists(data_file):
        os.makedirs(os.path.dirname(data_file), exist_ok=True)
        # Generate random sales data
        dummy_data = np.random.normal(loc=5000, scale=1500, size=100)
        np.savetxt(data_file, dummy_data, header="Sales", comments='', delimiter=',')
        print("Generated dummy sales data.")

    calc = StatsCalculator(data_file)
    calc.load_data()
    calc.analyze()
    calc.print_report()

if __name__ == "__main__":
    main()
