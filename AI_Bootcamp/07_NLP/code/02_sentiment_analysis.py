from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def main():
    print("=== Simple Sentiment Analysis ===\n")

    # Data Training Sederhana
    train_sentences = [
        "I love this product, it is amazing",
        "This is the best service ever",
        "I feel happy using this app",
        "Terrible experience, I hate it",
        "The product is broken and bad",
        "I am very disappointed and angry"
    ]
    train_labels = ["Positive", "Positive", "Positive", "Negative", "Negative", "Negative"]

    # 1. Bag of Words (CountVectorizer)
    print("Training Model...")
    # Pipeline: Text -> Vector -> Classifier
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(train_sentences, train_labels)

    # 2. Prediction
    test_sentences = [
        "This is a good day",
        "I hate waiting so long",
        "Amazing features"
    ]
    
    print("\nPredictions:")
    predictions = model.predict(test_sentences)
    for text, label in zip(test_sentences, predictions):
        print(f"'{text}' -> {label}")

    # 3. TF-IDF Concept
    print("\n--- TF-IDF Vectorizer Demo ---")
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(train_sentences)
    print("Feature Names:", tfidf.get_feature_names_out())
    print("TF-IDF Matrix Shape:", tfidf_matrix.shape)

if __name__ == "__main__":
    main()
