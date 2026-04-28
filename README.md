# Wizard Intelligence Platform

## Project Vision

This project is part of a larger goal: building a full-stack, end-to-end AI system inspired by the Harry Potter universe.

The current implementation focuses on **spell classification**, but the long-term vision is to expand this into a broader platform that integrates:

- machine learning models
- data pipelines
- backend APIs
- interactive frontend experiences

---

## Planned Features

Future components of this platform include:

- **Sorting Hat Model**
  - Classify users into Hogwarts houses based on personality data

- **Spell Recommendation System**
  - Suggest spells based on user traits or context (content-based filtering)

- **Wizarding World Analytics Dashboard**
  - Visualize patterns in spells, houses, and character traits

- **Character Chat Interface**
  - Interact with AI personas (e.g., Hermione, Snape) using NLP

- **Audio Processing (Future)**
  - Detect speech vs magic-related content (ties into audio ML work)

---

## Current Module: Spell Classifier

The current version implements a baseline NLP classifier that predicts whether a spell is:

- `dark`
- `non-dark`

This module demonstrates:

- data cleaning and preprocessing
- feature engineering (TF-IDF)
- model training and evaluation
- API deployment with FastAPI
- frontend integration

This serves as the foundation for expanding the system into more advanced ML applications.
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