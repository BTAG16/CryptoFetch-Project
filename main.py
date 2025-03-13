import requests
import pandas as pd
from datetime import datetime

# Your CoinMarketCap API Key
API_KEY = "ad84cb58-a213-4abd-9486-a415377d66a1"
symbol = input("Enter your Symbol(e.g. BTC, ADA): ")

def fetch_latest_crypto_data(c_symbol, c_convert):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {'X-CMC_PRO_API_KEY': API_KEY}
    params = {
        'symbol': c_symbol,
        'convert': c_convert,
    }
    response = requests.get(url, headers=headers, params=params)
    c_data = response.json()
    if response.status_code == 200:
        quote = c_data['data'][f'{c_symbol}']['quote'][f'{c_convert}']
        return {
            'timestamp': datetime.now(),
            'price': quote['price'],
            'volume_24h': quote['volume_24h'],
            'market_cap': quote['market_cap']
        }
    else:
        print(f"Error fetching data: {c_data}")
        return None

def save_to_csv(coin_data, filename=f'{symbol}_USDT_data.csv'):
    df = pd.DataFrame([coin_data])
    try:
        # Append to existing file if it exists
        df.to_csv(filename, mode='a', header=False, index=False)
    except FileNotFoundError:
        # If file doesn't exist, create it with headers
        df.to_csv(filename, mode='w', header=True, index=False)

def fetch_and_save():
    global symbol
    convert = 'USDT'
    data = fetch_latest_crypto_data(symbol, convert)
    if data:
        save_to_csv(data)
        print("Data saved:", data)


fetch_and_save()
