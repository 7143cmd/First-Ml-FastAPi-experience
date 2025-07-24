import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

train_data = [
    ("you", 0),
    ("this", 0),
    ("is", 0),
    ("a", 0),
    ("are", 0),
    ("but", 0),
    ("asshole", 1),
    ("bitch", 1),
    ("that", 0),
    ("guy", 0),
    ("wonderful", 0),
    ("day", 0),
    ("good", 0),
    ("nice", 0),
    ("excellent", 0),
    ("happy", 0),
    ("fuck", 1),
    ("fucking", 1),
    ("shit", 1),
    ("bitch", 1),
    ("damn", 1),
    ("crap", 1),
    ("hell", 1),
    ("dick", 1),
    ("piss", 1),
    ("bastard", 1),
    ("pleasant", 0),
    ("awesome", 0),
    ("terrific", 0),
    ("idiot", 1),
    ("moron", 1)
]

X_train = [text for text, label in train_data]
y_train = [label for text, label in train_data]

model = Pipeline([
    ('vectorizer', CountVectorizer(analyzer='word')),
    ('classifier', LogisticRegression())
])

model.fit(X_train, y_train)

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

# test_text = "This is a wonderful day but that guy is a fucking asshole!"
# filtered_text = filter_text(test_text)
print("Filtered text:", filter_text("You are asshole bitch!"))