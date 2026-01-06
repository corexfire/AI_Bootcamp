import json
import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

class NLPEngine:
    def __init__(self, data_path=None, model_path=None):
        # Resolve paths relative to the project root
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        self.data_path = data_path or os.path.join(base_dir, "data", "intents_large.json")
        self.model_path = model_path or os.path.join(base_dir, "data", "model.pkl")
        
        # Fallback to intents.json if intents_large.json doesn't exist
        if not os.path.exists(self.data_path) and data_path is None:
             self.data_path = os.path.join(base_dir, "data", "intents.json")

        self.pipeline = None
        self.intents = []
        
        self.load_data()
        
    def load_data(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Intents file not found at {self.data_path}")
            
        with open(self.data_path, 'r') as f:
            self.intents = json.load(f)['intents']

    def train(self):
        print("Training NLP Model (Multilingual + Typo Robust)...")
        corpus = []
        labels = []
        
        for intent in self.intents:
            # Flatten patterns from all languages
            for lang, patterns in intent['patterns'].items():
                for pattern in patterns:
                    corpus.append(pattern)
                    labels.append(intent['tag'])
                
        # Robust Pipeline: Character N-Grams + Logistic Regression
        # analyzer='char_wb' breaks text into character n-grams inside word boundaries.
        # This makes the model resilient to typos (e.g., "hello" and "helo" share many n-grams).
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 5))), 
            ('clf', LogisticRegression(random_state=42, max_iter=1000))
        ])
        
        self.pipeline.fit(corpus, labels)
        print("Model Trained Successfully.")
        
        # Save model
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.pipeline, f)

    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, 'rb') as f:
                self.pipeline = pickle.load(f)
        else:
            self.train()

    def predict(self, text):
        if not self.pipeline:
            self.load_model()
            
        # Get probability
        probs = self.pipeline.predict_proba([text])[0]
        max_prob = np.max(probs)
        pred_idx = np.argmax(probs)
        pred_tag = self.pipeline.classes_[pred_idx]
        
        return pred_tag, max_prob

    def get_response(self, tag, lang='en'):
        for intent in self.intents:
            if intent['tag'] == tag:
                # Get response based on language, fallback to 'en' if 'id' not found
                responses = intent['responses'].get(lang, intent['responses'].get('en', []))
                return np.random.choice(responses), intent.get('context_set', "")
        
        fallback_msg = {
            'en': "I'm not sure how to respond to that.",
            'id': "Saya kurang mengerti maksud Anda."
        }
        return fallback_msg.get(lang, fallback_msg['en']), ""

# Singleton Instance
nlp_engine = NLPEngine()
