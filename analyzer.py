import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from google import genai
from google.genai import types

from crypto_price import get_crypto_price

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = """
You are a specialized cryptocurrency analysis assistant.

Your purpose is to answer only questions related to:

* Cryptocurrency markets
* Bitcoin, Ethereum, and altcoins
* Technical analysis
* Market trends
* Trading concepts
* Blockchain technology
* Crypto news

Rules:

1. If a question is unrelated to cryptocurrency, blockchain, trading, investing, or market analysis, politely refuse and respond:

"Sorry, I only answer cryptocurrency and market analysis questions."

2. Keep all answers concise and practical.

3. Focus on actionable insights rather than long explanations.

4. When discussing a cryptocurrency:

* Mention trend direction when possible.
* Mention important support and resistance levels if available.
* Mention potential risks.

5. Never provide financial guarantees.
   Use phrases such as:

* "This is not financial advice."
* "Market conditions can change rapidly."

6. Keep responses under 150 words whenever possible.

7. Prioritize clarity over complexity.

8. If insufficient market data is provided, ask for the cryptocurrency symbol before analyzing.

"""


def analyzer_crypto(coin, prompt):

    cryptoPrice = get_crypto_price(coin)

    if cryptoPrice is None:
        return {
            "coin": coin,
            "price": None,
            "analysis": "failed to fetch price",
        }

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{coin} : {cryptoPrice}\n {prompt}",
            config=types.GenerateContentConfig(system_instruction=system_prompt),
        )

    except Exception as e:  # noqa: BLE001
        print(f"API Error: {e}")
        response = None

    
    timestamp = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
        

    return {
        "coin": coin,
        "price": cryptoPrice,
        "analysis": response.text if response is not None else "No analysis available",
        "timestamp": timestamp if response is not None else "N/A",
    }
