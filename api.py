from analyzer import analyzer_crypto
from fastapi import FastAPI

app = FastAPI()


@app.get("/analyze")
def analyze(coin: str, prompt: str = "give me a brief analysis"):
    return analyzer_crypto(coin, prompt)
