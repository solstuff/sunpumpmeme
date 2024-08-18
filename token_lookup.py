import requests
from datetime import datetime

url = "https://api.sunpump.meme/pump-api/token/TLzqHxnsGSmax5NVVQveiJeAv3xzcqix6P"

data = requests.get(url).json()

if data["msg"] == "SUCCESS":
    timestamp = datetime.fromtimestamp(data["data"]["tokenLaunchedInstant"])

    print("Contract:", data["data"]["contractAddress"])
    print("Name:", data["data"]["name"])
    if data["data"]["twitterUrl"]: print("Twitter:", data["data"]["twitterUrl"])
    if data["data"]["telegramUrl"]: print("Telegram:", data["data"]["telegramUrl"])
    if data["data"]["websiteUrl"]: print("Website:", data["data"]["websiteUrl"])
    print("Launch Date:", timestamp)
