import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_crypto_price(symbol="btc"):

    try:
        response = requests.get(
            f"https://api.freecryptoapi.com/v1/getData?symbol={symbol}",
            headers={"Authorization": f"Bearer {os.getenv('CRYPTO_PRICE_API_KEY')}"},
        )
        response.raise_for_status()
        jsonData = response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

    item = jsonData["symbols"]

    return item[0]["last"]


if __name__ == "__main__":
    print(get_crypto_price("btc"))
