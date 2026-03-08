"""
 Challenge: Crypto Price Tracker with Graphs

Goal:
- Fetch live prices of the top 10 cryptocurrencies using CoinGecko's free public API
- Store prices in a CSV file with timestamp
- Generate a line graph for a selected coin over time (price vs. time)
- Repeatable — user can run this multiple times to log data over time

JSON handling, API usage, CSV storage, matplotlib graphing
"""

import os
import csv
import requests
from datetime import datetime
import matplotlib.pyplot as plt


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
    
    
            
def generate_graph(coin_name):
    timestamps = []
    prices = []
    if not os.path.isfile(FILE_NAME):
        print("No data file found. Please fetch data first.")
        return
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            timestamp, coin, price = row
            if coin != coin_name:
                continue
            timestamps.append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))
            prices.append(float(price))
            
    if not timestamps:
        print(f"No data found for {coin_name}.")
        return
    
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, prices, marker='o')
    plt.title(f"{coin_name} Price Over Time")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
     
       
def main():
    while True:
        print("Fetching crypto prices...")
        print("1. Fetching data.")
        print("2. Clean the data.")
        print("3. View graph.")
        print("4. Exit.")
    
        choice = input("Enter your choice: ")
    
        match choice:
            case "1":
                data = fetch_crypto_prices()
                if data:
                    save_to_csv(data)
                    print("Data fetched and saved successfully.")
                else:
                    print("Failed to fetch data.")
            case "2":
                print("Cleaning the data...")
                os.remove(FILE_NAME) if os.path.exists(FILE_NAME) else print("No data file to clean.")
                print("Data cleaned successfully.")
            case "3":
                coin_name = input("Enter the coin name to view graph (e.g., bitcoin): ").strip().lower()
                generate_graph(coin_name)
            case "4":
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
