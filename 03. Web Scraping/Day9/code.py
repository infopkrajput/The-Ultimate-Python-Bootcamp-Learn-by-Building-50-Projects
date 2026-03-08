"""
 Challenge: Store & Search Crypto Prices in SQLite

Goal:
- Save hourly top 10 crypto prices into a local SQLite database
- Each record should include timestamp, coin ID, and price
- Allow the user to search for a coin by name and return the latest price

Teaches: SQLite handling in Python, data storage, search queries, API + DB integration
"""

import os
import requests
import sqlite3
from datetime import datetime
import schedule
import time

BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"
FILE_NAME = "database.db"

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
    
    
def create_table():
    conn = sqlite3.connect(FILE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS crypto_prices(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       timestamp TEXT,
                       name TEXT,
                       price REAL)
                   ''')
    conn.commit()
    conn.close()
    
def save_data(data):
    conn = sqlite3.connect(FILE_NAME)
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for coin in data:
        cursor.execute('''
                       INSERT INTO crypto_prices (timestamp, name, price)
                       VALUES (?, ?, ?)
                       ''',(timestamp, coin['id'], coin['current_price']))
    conn.commit()
    conn.close()
    print(F"Data saved to database successfully.")
    
def search_coin(coin_name):
    conn = sqlite3.connect(FILE_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
                   SELECT timestamp, price FROM crypto_prices
                   WHERE name = ?
                   ORDER BY timestamp DESC
                   LIMIT 1
                   ''',(coin_name,))
    
    result = cursor.fetchone()
    conn.close()
    # print(f"Result: {result}")
    if result:
        print(f"Price of {coin_name} at {result[0]} : ${result[1]}")
        print("*" * 30)
    else:
        print(f"No data found for {coin_name}")
        print("*" * 30)
    
        
    
        
def main():
    create_table()
    while True:
        print("1. Fetch and store data.")
        print("2. Search latest price for a coin.")
        print("3. Exit.")
        
        choice = int(input("Enter your choice: ").strip())
        
        match choice:
            case 1:
                data = fetch_crypto_prices()
                save_data(data)
            case 2:
                name = input("Enter the name of coin: ").strip().lower()
                search_coin(name)
            case 3:
                break
            case _:
                print("Please choose a valid option.")
                

if __name__ == "__main__":
    main()