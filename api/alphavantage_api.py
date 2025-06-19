# https://www.alphavantage.co/documentation/
import requests

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='../envfile/.envkeys')
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
if not API_KEY:
    raise ValueError("API key for Alpha Vantage is not set in the environment variables.")
# Example usage of Alpha Vantage API to get intraday stock data
symbol = "IBM"
#url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}"
url=f"https://www.alphavantage.co/query?function=TIME_SERIESTIME_SERIES_WEEKLY_DAILY&symbol={symbol}&apikey={API_KEY}"
response = requests.get(url)
data = response.json()
print(data)
