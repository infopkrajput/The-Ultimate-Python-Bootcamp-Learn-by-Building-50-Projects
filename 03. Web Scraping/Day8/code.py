"""
depends on:
 - Day 7 of web scraping

Fetch crypto data every hour automatically

"""
import os
import csv
import requests
from datetime import datetime
import schedule
import time

BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"
FILE_NAME = "crypto_prices.csv"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False,
}

def fetch_crypto_prices():
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None
    
    
def save_to_csv(data):
    file_exists = os.path.isfile(FILE_NAME)
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for coin in data:
            writer.writerow([timestamp, coin['id'], coin['current_price']])
        
        
def job():
    print(f"Fetching data successfully at {datetime.now().strftime("%H:%M:%S")}")
    data = fetch_crypto_prices()
    if data:
        save_to_csv(data)
        # print("Data fetched and saved successfully.")
    else:
        print("Failed to fetch data.")
    
    
schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
    
