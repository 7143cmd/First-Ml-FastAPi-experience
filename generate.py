import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import sqlite3
import joblib  
import os

MODEL_PATH = "bad_words_model.pkl"
def load_From_Db():
    conn = sqlite3.connect("train_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT text, label FROM words")
    rows = cursor.fetchall()
    conn.close()
    X_train = [text for text, label in rows]
    Y_train = [label for text, label in rows]

    return X_train, Y_train
def train_and_save_model():
    
    X_train, Y_train = load_From_Db()

    model = Pipeline([
    ('vectorizer', CountVectorizer(analyzer='char', ngram_range=(3, 5))),
    ('classifier', LogisticRegression(class_weight='balanced'))
])

    model.fit(X_train, Y_train)
    joblib.dump(model, MODEL_PATH)
    return model

if os.path.exists(MODEL_PATH):
    print("Loading model from cache...")
    model = joblib.load(MODEL_PATH)
else:
    print("Training model...")
    model = train_and_save_model()

def filter_text(text):
    words = text.split()
    filtered_words = []
    for word in words:
        prediction = model.predict([word.lower()])[0]
        filtered_words.append('#' * len(word) if prediction == 1 else word)
    return ' '.join(filtered_words)

# test_text = "you shit, i hate fuck, moron, and idiot and moron and loser jerk!"
# print("Vectorizer vocabulary:", model.named_steps['vectorizer'].vocabulary_)

# print("Original:", test_text)
# print("Filtered:", filter_text(test_text))