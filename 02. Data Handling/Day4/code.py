"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import os
import csv
from datetime import datetime
import requests

FILENAME = "weather_log.csv"
API_KEY = "your_openweathermap_api_key_here"  # Replace with your actual API key

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "City", "Temperature (°C)", "Condition"])

def log_weather():
    city_name = input("Enter city name: ")
    
    date = datetime.now().strftime("%d-%m-%Y")
    with open(FILENAME, "r", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["City"] == city_name and row["Date"] == date:
                print(f"Weather data for {city_name} already logged today.")
                return
   
    try:
      url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
      response = requests.get(url)
      data = response.json()
      if response.status_code != 200 or not data:
          print(f"Error fetching data for {city_name}. Please check the city name and try again.")
          return
       
      temp = round(float(data["main"]["temp"]) - 273.15, 2)
      condition = data["weather"][0]["main"]
      with open(FILENAME, "a", newline='', encoding="utf-8") as file:
          writer = csv.writer(file)
          writer.writerow([date, city_name, temp, condition])
      print(f"Weather data for {city_name} logged successfully.")
       
    except requests.exceptions.RequestException as e:
      print(f"Error fetching data: {e}")
      return


def view_logs():
      with open(FILENAME, "r", newline='', encoding="utf-8") as file:
         reader = csv.reader(file)
         print(f"{'Date':<12} {'City':<20} {'Temperature (°C)':<20} {'Condition':<15}")
         print("-" * 70)
         for row in reader:
             if row[0] != "Date":  # Skip header
               print(f"{row[0]:<12} {row[1]:<20} {row[2]:<20} {row[3]:<15}")
         print("-" * 70)
      
def show_stats():
      with open(FILENAME, "r", newline='', encoding="utf-8") as file:
         reader = csv.DictReader(file)
         temps = []
         conditions = {}
         for row in reader:
               temps.append(float(row["Temperature (°C)"]))
               condition = row["Condition"]
               conditions[condition] = conditions.get(condition, 0) + 1
         
         if temps:
               avg_temp = sum(temps) / len(temps)
               max_temp = max(temps)
               min_temp = min(temps)
               most_freq_condition = max(conditions, key=conditions.get)
               
               print(f"Average Temperature: {avg_temp:.2f} °C")
               print(f"Highest Temperature: {max_temp:.2f} °C")
               print(f"Lowest Temperature: {min_temp:.2f} °C")
               print(f"Most Frequent Condition: {most_freq_condition}")
         else:
               print("No weather data available to show stats.")
               
def main():
      while True:
         print("\n1. Log Weather")
         print("2. View Logs")
         print("3. Show Stats")
         print("4. Exit")
         
         choice = input("Enter your choice: ")
         
         match choice:
               case "1":
                     log_weather()
               case "2":
                     view_logs()
               case "3":
                     show_stats()
               case "4":
                     print("Exiting the program.")
                     break
               case _:
                     print("Invalid choice. Please try again.")
if __name__ == "__main__":      
   main()