import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os
import joblib

# MODEL_PATH = "bad_words_model.pkl"

# if os.path.exists(MODEL_PATH):
#     print("Loading model from cache...")
#     model = joblib.load(MODEL_PATH)

def filter_text(text):
    MODEL_PATH = "bad_words_model.pkl"
    if os.path.exists(MODEL_PATH):
        print("Loading model from cache...")
        model = joblib.load(MODEL_PATH)
        
    #print(f"Original text: {text}, \nprocessing...")
    words = text.split()
    filtered_words = []
    for word in words:
        prediction = model.predict([word.lower()])[0]

        # prob = model.predict_proba([word.lower()])
        # print(f"{word}, {prob}")

        if prediction == 1:
            filtered_words.append('#' * len(word))
        else:
            filtered_words.append(word)
    return ' '.join(filtered_words)
# def start(text):
#     reworked = filter_text(text)
#     print(F"Filtered text: {reworked}")


# text_text = "Do you like play football? I vote for the team named <<Shahtar>>"
# start(text_text)
