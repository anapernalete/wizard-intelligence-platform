from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "ml/models/spell_classifier.pkl")
vectorizer = joblib.load(BASE_DIR / "ml/models/tfidf_vectorizer.pkl")

class SpellRequest(BaseModel):
    description: str

@app.get("/")
def read_root():
    return {"message":"Wizard API is running!"}

@app.post("/predict-spell")
def predict_spell(request: SpellRequest):
    text = request.description.lower().strip()
    X_new = vectorizer.transform([text])
    prediction = model.predict(X_new)[0]
    
    return {
        "description": request.description,
        "prediction": prediction
    }