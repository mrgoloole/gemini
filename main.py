import os
from datetime import datetime, timezone
from time import sleep

from dotenv import load_dotenv
from google import genai

from crypto_price import get_crypto_price

load_dotenv()

running = True

while running:

    print("Welcome to the Gemini Chat!\n")

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    symbol_input = input(
        "Enter the symbol of the cryptocurrency you want to check (e.g., btc, eth): "
    )
    client_prompt = input("Ask Gemini a question about analysis current Crypto price: ")

    cryptoPrice = get_crypto_price(symbol_input)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{client_prompt}: {cryptoPrice}",
        )
    except (ConnectionError, ValueError, RuntimeError) as e:
        print(f"API Error: {e}")
        response = None

    if response is not None:
        timestamp = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
        print(f"{response.text}\n [{timestamp}]\n ")

    sleep(300)
