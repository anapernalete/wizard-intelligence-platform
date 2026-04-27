import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "ml/models/spell_classifier.pkl"
VECTORIZER_PATH = BASE_DIR / "ml/models/tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

DARK_KEYWORDS = [
    "avada kedavra",
    "killing curse",
    "crucio",
    "torture",
    "imperio",
    "unforgivable curse",
    "dark mark",
    "morsmordre",
    "sectumsempra",
    "fiendfyre",
]


def predict_text(text: str):
    text_clean = text.lower().strip()

    for keyword in DARK_KEYWORDS:
        if keyword in text_clean:
            return "dark"

    X_new = vectorizer.transform([text_clean])
    prediction = model.predict(X_new)[0]
    return prediction