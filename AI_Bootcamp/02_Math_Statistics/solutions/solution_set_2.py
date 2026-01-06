import numpy as np

def solve_matrix_ops():
    """Soal 1"""
    A = np.array([[2, 4], [1, 3]])
    B = np.array([[5, 1], [2, 6]])
    
    sum_mat = A + B
    dot_mat = A @ B
    trans_mat = dot_mat.T
    
    print("1. Sum:\n", sum_mat)
    print("   Dot:\n", dot_mat)
    print("   Transpose Dot:\n", trans_mat)

def solve_height_analysis():
    """Soal 2"""
    heights = np.array([165, 170, 155, 162, 180, 175, 168, 158])
    mean = np.mean(heights)
    std = np.std(heights)
    above_avg = heights[heights > mean]
    
    print("\n2. Mean:", mean)
    print("   Std Dev:", std)
    print("   Above Avg:", above_avg)

def min_max_scaling(data):
    """Soal 3"""
    min_val = np.min(data)
    max_val = np.max(data)
    if max_val - min_val == 0:
        return np.zeros_like(data)
    return (data - min_val) / (max_val - min_val)

def euclidean_distance(p1, p2):
    """Soal 4"""
    # p1 dan p2 adalah numpy array
    return np.linalg.norm(p1 - p2)
    # Atau manual: np.sqrt(np.sum((p1 - p2)**2))

if __name__ == "__main__":
    solve_matrix_ops()
    solve_height_analysis()
    
    data = np.array([10, 20, 30, 40, 50])
    print("\n3. MinMax Scaled:", min_max_scaling(data))
    
    p1 = np.array([1, 2])
    p2 = np.array([4, 6])
    print("\n4. Euclidean Dist:", euclidean_distance(p1, p2))
