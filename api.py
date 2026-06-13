import logging

from fastapi import FastAPI, HTTPException

from analyzer import analyzer_crypto

app = FastAPI()
logger = logging.getLogger(__name__)


@app.get("/analyze")
def analyze(coin: str, prompt: str = "give me a brief analysis"):
    if not coin or not coin.strip():
        raise HTTPException(status_code=400, detail="Coin symbol is required")

    if len(coin) > 10:
        raise HTTPException(status_code=400, detail="Coin symbol too long")

    if not prompt or not prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is required")

    if len(prompt) > 500:
        raise HTTPException(status_code=400, detail="Prompt too long (max 500 chars)")

    try:
        resault = analyzer_crypto(coin.lower().strip(), prompt.strip())
        if resault["analysis"] == "failed to fetch price":
            raise HTTPException(
                status_code=503, detail=f"Unable to fetch price for {coin}"
            )
        return resault
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
