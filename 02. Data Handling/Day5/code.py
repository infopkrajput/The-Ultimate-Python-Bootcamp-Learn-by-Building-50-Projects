"""
Sample data:
Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Plot graphs from this data
"""

import csv
import os
from collections import defaultdict as dd
import matplotlib.pyplot as plt

FILENAME = "weather_data.csv"

def visualize_weather_data(filename):
    dates = []
    temperature = []
    condition = dd(int)
    
    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                dates.append(row["Date"])
                temperature.append(float(row["Temperature"]))
                condition[row["Condition"]] += 1
            except (KeyError, ValueError):
                print(f"Skipping invalid row: {row}")
                
    if not dates or not temperature:
        print("No valid data to plot.")
        return
    plt.figure(figsize=(12, 6))
    plt.plot(dates, temperature, marker='o')
    plt.title("Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.grid(True)
    plt.show()
    
    
    plt.figure(figsize=(8, 6))
    plt.bar(condition.keys(), condition.values(), color='skyblue')
    plt.title("Weather Conditions")
    plt.xlabel("Condition")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    if os.path.exists(FILENAME):
        visualize_weather_data(FILENAME)
    else:
        print(f"File {FILENAME} not found.")

    