import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os

class MovieRecommender:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.cosine_sim = None

    def load_data(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError("Data file not found")
        
        self.df = pd.read_csv(self.data_path)
        print(f"Loaded {len(self.df)} movies.")
        print(self.df.head())

    def build_model(self):
        # Menggunakan TF-IDF pada Genre untuk menghitung kemiripan
        # Genre string: "Action|Adventure|Thriller" -> "Action Adventure Thriller"
        self.df['Genres_Clean'] = self.df['Genres'].str.replace('|', ' ')
        
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.df['Genres_Clean'])
        
        # Hitung Cosine Similarity antar film
        self.cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        print("\nModel built successfully (Cosine Similarity Matrix).")

    def recommend(self, title, top_n=5):
        # Cari index film berdasarkan judul
        try:
            idx = self.df[self.df['Title'].str.contains(title, case=False)].index[0]
        except IndexError:
            print(f"\nMovie '{title}' not found.")
            return

        print(f"\nCalculating recommendations for: {self.df.iloc[idx]['Title']}")
        
        # Ambil skor similarity untuk film tersebut
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        
        # Urutkan berdasarkan skor tertinggi
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Ambil top N (skip index 0 karena itu film itu sendiri)
        sim_scores = sim_scores[1:top_n+1]
        
        movie_indices = [i[0] for i in sim_scores]
        
        print("\nTop Recommendations:")
        for i, m_idx in enumerate(movie_indices):
            print(f"{i+1}. {self.df.iloc[m_idx]['Title']} (Genres: {self.df.iloc[m_idx]['Genres']})")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data', 'movies.csv')
    
    recsys = MovieRecommender(data_path)
    recsys.load_data()
    recsys.build_model()
    
    # Test Recommendation
    recsys.recommend('Toy Story')
    recsys.recommend('GoldenEye')

if __name__ == "__main__":
    main()
