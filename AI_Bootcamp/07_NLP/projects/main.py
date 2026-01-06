import json
import numpy as np
import random
import os
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier

# Pastikan NLTK resource tersedia
# nltk.download('punkt'); nltk.download('wordnet')

class SimpleChatbot:
    def __init__(self, intents_file):
        self.intents_file = intents_file
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = CountVectorizer()
        self.classifier = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)
        self.tags = []
        self.responses = {}

    def load_data(self):
        with open(self.intents_file, 'r') as f:
            data = json.load(f)

        corpus = []
        labels = []
        
        for intent in data['intents']:
            tag = intent['tag']
            self.tags.append(tag)
            self.responses[tag] = intent['responses']
            
            for pattern in intent['patterns']:
                # Preprocessing sederhana: Lowercase
                corpus.append(pattern.lower())
                labels.append(tag)
        
        return corpus, labels

    def train(self):
        print("Training Chatbot...")
        corpus, labels = self.load_data()
        
        # Vectorize Text (Bag of Words)
        X = self.vectorizer.fit_transform(corpus)
        y = labels
        
        # Train Classifier (Neural Network sederhana)
        self.classifier.fit(X, y)
        print("Chatbot Ready!")

    def get_response(self, user_input):
        # Preprocess input
        input_vec = self.vectorizer.transform([user_input.lower()])
        
        # Predict tag
        pred_tag = self.classifier.predict(input_vec)[0]
        probs = self.classifier.predict_proba(input_vec)
        
        # Confidence threshold (optional simple logic)
        max_prob = np.max(probs)
        if max_prob < 0.5:
            return "I'm sorry, I don't understand."
            
        # Return random response from tag
        return random.choice(self.responses[pred_tag])

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data', 'intents.json')
    
    bot = SimpleChatbot(data_path)
    bot.train()
    
    print("\n=== AI Chatbot Demo (Type 'quit' to exit) ===")
    print("Bot: Hello! Ask me anything.")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Bot: Goodbye!")
                break
            
            response = bot.get_response(user_input)
            print(f"Bot: {response}")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
