# Wizard Intelligence Platform

## Project Summary

## Project Summary

Built an end-to-end NLP classification system inspired by the Harry Potter universe to classify spells as `dark` or `non-dark`. Leveraged Python, scikit-learn, and TF-IDF for text processing, deployed the model using FastAPI, and integrated it with a frontend interface for real-time predictions.

---

## Overview

This project demonstrates a complete ML pipeline:

- Data collection and cleaning
- Feature engineering (TF-IDF)
- Text classification model (Logistic Regression)
- FastAPI backend for predictions
- Simple frontend interface for user interaction

---

## How It Works

1. User enters a spell description
2. Frontend sends request to FastAPI backend
3. Backend processes text using trained vectorizer
4. ML model predicts:
   - `dark`
   - `non-dark`
5. Result is returned and displayed

---

## Example

**Input:**
Avada Kedavra killing curse

**Output:**
dark

---
## FastAPI Backend

The project includes a FastAPI backend that serves the spell classification model.

---

## Run Locally

### 1. Activate environment

```bash
source venv/bin/activate
```
### 2. Start backend
```bash
uvicorn backend.main:app --reload
```
### 3. Open API docs
http://127.0.0.1:8000/docs

### 4. Open frontend
frontend/index.html

### API Endpoints

- `GET /`  
  Returns a basic API status message.

- `GET /health`  
  Returns API health status.

- `POST /predict-spell`  
  Predicts whether a spell description is `dark` or `non-dark`.

### Example Request

```json
{
  "description": "causes unbearable pain"
}
```
### Example Response
```json
{
  "description": "causes unbearable pain",
  "prediction": "dark"
}
```

### Model Notes
* Model: Logistic Regression
* Features: TF-IDF vectorization
* Evaluation: Cross-validation (macro F1 ≈ 0.48)

#### Limitations
* Small dataset (~70 samples)
* Class imbalance (few dark spells)
* Model tends to favor majority class