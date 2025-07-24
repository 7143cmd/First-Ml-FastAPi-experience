import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os
import joblib

MODEL_PATH = "bad_words_model.pkl"

if os.path.exists(MODEL_PATH):
    print("Loading model from cache...")
    model = joblib.load(MODEL_PATH)

def filter_text(text):
    print("Original text:", text)
    print("processing...")
    words = text.split()
    filtered_words = []
    for word in words:
        prediction = model.predict([word.lower()])[0]
        if prediction == 1:
            filtered_words.append('#' * len(word))
        else:
            filtered_words.append(word)
    return ' '.join(filtered_words)
def start():
    # Сначала обучаем модель

    # Потом фильтруем текст
    print("Filtered text:", filter_text("Fuckin moron, stop doing shit, asshole!"))

start()
