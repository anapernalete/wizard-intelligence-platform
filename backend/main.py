from fastapi import FastAPI
from backend.schemas import SpellRequest
from backend.model_utils import predict_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Wizard API is running!"}

@app.post("/predict-spell")
def predict_spell(request: SpellRequest):
    prediction = predict_text(request.description)
    
    return {
        "description": request.description,
        "prediction": prediction
    }