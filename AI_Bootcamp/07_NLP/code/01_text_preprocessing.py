import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# Download resource NLTK (perlu dijalankan sekali)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

def main():
    print("=== Text Preprocessing Demo ===\n")
    
    text = "Hello! AI Bootcamp is amazing. The students are learning very fast, running code everywhere."
    print(f"Original Text: {text}")

    # 1. Lowercasing
    text = text.lower()
    print(f"\nLowercased: {text}")

    # 2. Tokenization
    # Jika punkt belum ada, kita pakai split sederhana untuk demo aman
    try:
        tokens = word_tokenize(text)
    except LookupError:
        print("(NLTK punkt not found, using split)")
        tokens = text.split()
    
    print(f"Tokens: {tokens}")

    # 3. Remove Punctuation
    tokens = [word for word in tokens if word.isalnum()]
    print(f"No Punctuation: {tokens}")

    # 4. Remove Stopwords
    try:
        stop_words = set(stopwords.words('english'))
        tokens = [w for w in tokens if not w in stop_words]
        print(f"No Stopwords: {tokens}")
    except LookupError:
        print("(NLTK stopwords not found, skipping step)")

    # 5. Stemming (Mengubah ke kata dasar kasar: running -> run)
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(word) for word in tokens]
    print(f"Stemmed: {stemmed}")

    # 6. Lemmatization (Mengubah ke kata dasar kamus: better -> good)
    try:
        lemmatizer = WordNetLemmatizer()
        lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
        print(f"Lemmatized: {lemmatized}")
    except LookupError:
        print("(NLTK wordnet not found, skipping step)")

if __name__ == "__main__":
    # Uncomment baris ini jika menjalankan pertama kali dan punya koneksi internet
    # nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')
    main()
