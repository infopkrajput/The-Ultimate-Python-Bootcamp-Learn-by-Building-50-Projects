"""
 Challenge: CSV-TO-JSON Converter Tool

"""

import os 
import json
import csv


FILENAME = "csv_data.csv"
OUTPUT_FILE = "output_file.json"

def load_csv(data):
    if not os.path.exists(data):
        print("CSV file not exists!")
        return []
    
    with open(data,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data


    
def convert_csv_to_json(data,output):
    with open(output,"w",encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    
    print(f"Converted {len(data)} record to {output}")

def main():
    data = load_csv(FILENAME)
    if not data:
        print("There is no data in CSV!")
        return
    convert_csv_to_json(data,OUTPUT_FILE)
    
if __name__ == "__main__":
    main()