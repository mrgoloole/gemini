# Crypto AI Analyzer

Real-time cryptocurrency price analyzer powered by Google Gemini AI.

## Features
- Fetches live crypto prices
- AI-powered price analysis via Gemini
- Configurable update interval
- Supports multiple coins

## Setup
1. Clone the repo
2. Create `.env` file (see `.env.example`)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`

## Tech Stack
- Python
- Google Gemini API
- freecryptoapi

## Live API
- Base URL: https://gemini-production-34e7.up.railway.app

### Endpoints
- GET /analyze?coin=btc
- GET /analyze?coin=eth&prompt=what is the trend?

### Docs
- https://gemini-production-34e7.up.railway.app/docs