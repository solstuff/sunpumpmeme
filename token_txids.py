import requests

url = "https://api.sunpump.meme/pump-api/transactions/token/TCR2f2EZEriqFV2b6nfnsZ7TUcVRyx8U8S?page=1&size=5&sort=volumeInUsd:DESC"


data = requests.get(url).json()["data"]["swaps"]
for tx in data:
    print("Address:", tx['userAddress'])
    print(f"Amount: ${tx['volumeInUsd']:,.2f}")
    print("Event:", tx['txnOrderType'])

print("Top 5 biggest transactions for", tx['toTokenSymbol'])
