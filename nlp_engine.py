import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict(msg):
    vec = vectorizer.transform([msg])
    probs = model.predict_proba(vec)[0]

    confidence = max(probs)
    intent = model.classes_[probs.argmax()]

    return intent, confidence