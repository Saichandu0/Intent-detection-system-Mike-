
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import re
import nltk_init  # Ensure required NLTK data is available

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return ' '.join(text.split())

class IntentDetector:
    def __init__(self, training_sentences, training_labels):
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.classifier = LogisticRegression(max_iter=1000)

        # Preprocess and train
        self.processed_sentences = [preprocess_text(sentence) for sentence in training_sentences]
        X = self.vectorizer.fit_transform(self.processed_sentences)
        self.classifier.fit(X, training_labels)

    def predict_intent(self, text):
        if not text:
            return "unknown"
        processed = preprocess_text(text)
        try:
            X_test = self.vectorizer.transform([processed])
            return self.classifier.predict(X_test)[0]
        except:
            return "unknown"
