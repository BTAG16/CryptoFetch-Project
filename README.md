# Cryptocurrency Price Tracker

This Python script fetches real-time cryptocurrency price data using the CoinMarketCap API and saves it to a CSV file for further analysis.

## Features
- Fetches real-time cryptocurrency prices.
- Saves the data with timestamp, price, 24h volume, and market cap.
- Appends new data to an existing CSV file.
- Uses CoinMarketCap API for data retrieval.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `requests`
  - `pandas`
  - `python-dotenv`

You can install them using:
```bash
pip install requests pandas python-dotenv
```

## Setup
1. Get a free API key from [CoinMarketCap](https://coinmarketcap.com/api/).
2. Create a `.env` file in the same directory as the script and add your API key:
   ```
   API=your_coinmarketcap_api_key
   ```
3. Run the script and enter the cryptocurrency symbol when prompted:
   ```bash
   python crypto_tracker.py
   ```

## Usage
- The script prompts the user to enter a cryptocurrency symbol (e.g., BTC, ADA).
- It fetches the latest price data in USDT (Tether) from CoinMarketCap.
- The data is saved in a CSV file named `<symbol>_USDT_data.csv`.

## Example Output
```
Enter your Symbol(e.g. BTC, ADA): BTC
Data saved: {'timestamp': '2025-03-13 12:34:56', 'price': 65000, 'volume_24h': 32000000000, 'market_cap': 1200000000000}
```

### License
This project is open-source and available under the MIT License.

