from collections import Counter
import re

def solve_theory():
    print("--- Theory Answers ---")
    print("1. Tokenization: Proses memecah teks menjadi unit kecil (token). Word token: 'I love AI' -> ['I', 'love', 'AI']. Sentence token: 'Hi. Bye.' -> ['Hi.', 'Bye.'].")
    print("2. Stopwords dihapus untuk mengurangi noise dan dimensi data karena tidak membawa banyak makna topik. Penting dipertahankan untuk: Grammar checking, Phrase matching tepat, atau Sentiment analysis yang sensitif konteks (misal 'not').")
    print("3. Kelemahan BoW: Tidak menangkap urutan kata (context) dan makna semantik (kata 'king' dan 'queen' dianggap tidak berhubungan). Word Embedding menangkap hubungan semantik dalam ruang vektor.")
    print("5. Dokumen A: 'Sky is blue' (3 kata). Kata 'Sky' muncul 1 kali. TF = 1/3 = 0.33.")

def solve_coding_challenge():
    print("\n--- Soal 4: Top 5 Frequent Words ---")
    text = """
    Artificial Intelligence is intelligence demonstrated by machines. 
    AI is widely used in industry. Machine learning is a subset of AI. 
    Deep learning is a subset of machine learning.
    """
    
    # Simple preprocessing
    text = text.lower()
    words = re.findall(r'\w+', text) # Regex untuk ambil kata saja
    
    # Dummy stopwords list
    stopwords = {'is', 'a', 'of', 'in', 'by', 'the'}
    
    filtered_words = [w for w in words if w not in stopwords]
    
    # Count
    counter = Counter(filtered_words)
    print("Top 5 Words:", counter.most_common(5))

if __name__ == "__main__":
    solve_theory()
    solve_coding_challenge()
