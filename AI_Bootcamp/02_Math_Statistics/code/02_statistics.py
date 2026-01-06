import numpy as np
from scipy import stats

def main():
    print("=== Statistik Deskriptif Dasar ===\n")
    
    data = np.array([12, 15, 12, 10, 15, 18, 20, 22, 25, 15])
    print(f"Data: {data}")
    
    # 1. Central Tendency (Pusat Data)
    mean_val = np.mean(data)
    median_val = np.median(data)
    mode_val = stats.mode(data, keepdims=True).mode[0]
    
    print(f"Mean (Rata-rata): {mean_val}")
    print(f"Median (Nilai Tengah): {median_val}")
    print(f"Mode (Modus): {mode_val}")
    
    # 2. Dispersion (Penyebaran Data)
    variance = np.var(data)
    std_dev = np.std(data)
    min_val = np.min(data)
    max_val = np.max(data)
    range_val = max_val - min_val
    
    print("\n--- Penyebaran ---")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Range: {range_val} ({min_val} - {max_val})")
    
    # 3. Percentiles
    p25 = np.percentile(data, 25)
    p75 = np.percentile(data, 75)
    iqr = p75 - p25
    
    print("\n--- Percentiles ---")
    print(f"Q1 (25%): {p25}")
    print(f"Q3 (75%): {p75}")
    print(f"IQR (Interquartile Range): {iqr}")

if __name__ == "__main__":
    main()
