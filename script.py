import requests

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Datos: ", data)
else:
    print("Error: ", response.status_code)