import requests
from bs4 import BeautifulSoup

url_trans = f"https://transferwise.com/gb/currency-converter/khr-to-usd-rate?amount=1000"
request = requests.get(url_trans)

soup = BeautifulSoup(request.text, "html.parser")

input_group = soup.find("input", {"class": "js-TargetAmount"})["value"]


print(input_group)
