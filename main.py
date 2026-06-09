from time import sleep

from analyzer import analyzer_crypto

running = True


print("Welcome to the Gemini Chat!\n")

coin = input("Enter the symbol of the cryptocurrency you want to check (btc, eth): ")
prompt = input("Ask Gemini a question about analysis current Crypto price: ")

interval = input("Update interval in seconds (default 300): ")
interval = int(interval) if interval else 300

while running:
    resault = analyzer_crypto(coin, prompt)
    print(f"{resault["analysis"]}")
    print(f"[{resault['timestamp']}]")
    print("-" * 50)

    try:
        sleep(interval)
    except KeyboardInterrupt:
        print("Exiting Gemini Chat. Goodbye!")
        running = False
