import requests

url = "https://api.sunpump.meme/pump-api/token/holders?page=%d&size=10&address=TXL6rJbvmjD46zeN1JssfgxvSo99qC8MRT"

X = 0
for _ in range(2):
    X += 1
    data = requests.get(url % (X)).json()["data"]["holders"]
    print(f"\nPage {X}")
    for holder in data:
        print(f"Address: {holder['address']}\nPercentage: {holder['percentage']:,.1f}%")
        if holder["holderType"] != "NORMAL_USER": print("Who.is:", holder["holderType"])
