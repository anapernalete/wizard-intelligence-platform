from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import SpellRequest
from backend.model_utils import predict_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message":"Wizard API is running!"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True
    }

@app.post("/predict-spell")
def predict_spell(request: SpellRequest):
    prediction = predict_text(request.description)
    
    return {
        "description": request.description,
        "prediction": prediction
    }