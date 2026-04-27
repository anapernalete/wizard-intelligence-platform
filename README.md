# Wizard Intelligence Platform

An end-to-end Harry Potter-inspired data science and AI project.

This project will include:

- Data collection
- Data cleaning
- Exploratory data analysis
- Machine learning models
- FastAPI backend
- Frontend interface
- AI-powered features

---
## FastAPI Backend

The project includes a FastAPI backend that serves the spell classification model.

### Endpoints

- `GET /`  
  Returns a basic API status message.

- `GET /health`  
  Returns API health status.

- `POST /predict-spell`  
  Predicts whether a spell description is `dark` or `non-dark`.

### Example Request

```json
{
  "description": "Avada Kedavra killing curse"
}

### Example Response
```json
{
  "description": "Avada Kedavra killing curse",
  "prediction": "dark"
}

### Run the API locally
uvicorn backend.main:app --reload

Then open:
http://127.0.0.1:8000/docs

WIP