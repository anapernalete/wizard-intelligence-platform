# Data Sources

## Goal

This project will use multiple data sources to build an end-to-end Harry Potter-inspired data science and AI platform.

## Planned data sources

1. Structured public data
   - Characters
   - Houses
   - Spells
   - Wand/core information if available

2. Scraped / collected text data
   - Character descriptions
   - Spell descriptions
   - House trait descriptions

3. Synthetic data
   - Sorting Hat personality dataset
   - User quiz answers
   - House labels

## Data science tasks

- Collect raw data
- Store raw data in `data/raw/`
- Clean and standardize data
- Save cleaned data in `data/processed/`
- Generate synthetic training data in `data/synthetic/`
- Create EDA notebooks
- Build ML models

## Source 1: Harry Potter Spells Compendium

- Source: Kaggle
- Data type: Structured spell data
- Raw file: `data/raw/spells.csv`
- Planned use:
  - Spell cleaning
  - Spell category analysis
  - NLP on spell effects
  - Spell recommender system

WIP