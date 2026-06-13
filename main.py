import logging
from time import sleep

from analyzer import analyzer_crypto

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

running = True

print("Welcome to the Gemini Chat!\n")

coin = input("Enter the symbol of the cryptocurrency you want to check (btc, eth): ")
prompt = input("Ask Gemini a question about analysis current Crypto price: ")

while True:
    try:
        interval_input = input("Update interval in seconds (default 300): ")
        interval = int(interval_input) if interval_input else 300
        if interval < 1:
            print("Interval must be at least 1 second. Using default 300.")
            interval = 300
        break
    except ValueError:
        print("Invalid input. Please enter a number. Using default 300.")
        interval = 300
        break

logger.info(f"Starting analysis for {coin} with interval {interval}s")

while running:
    try:
        result = analyzer_crypto(coin, prompt)
        logger.info(f"Analysis completed for {coin}")
        print("-" * 50)
        print(f"{result['analysis']}")
        print(f"[{result['timestamp']}]")
        print("-" * 50)
        sleep(interval)
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
        print("Exiting Gemini Chat. Goodbye!")
        running = False
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Error: {e}")
