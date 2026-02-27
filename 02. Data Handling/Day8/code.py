"""
Challenge : JSON Flattener

{
  "user": {
    "id": 1,
    "name": "Riya",
    "email": "riya@example.com",
    "address": {
      "city": "Delhi",
      "pincode": 110001
    }
  },
  "roles": ["admin", "editor"],
  "is_active": true
}

Flatten this to:

{
  "user.id": 1,
  "user.name": "Riya",
  "user.email": "riya@example.com",
  "user.address.city": "Delhi",
  "user.address.pincode": 110001,
  "roles.0": "admin",
  "roles.1": "editor",
  "is_active": true
}

"""

import json 
import os 

INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "output_file.json"

def flatten_data(data, sep=".",parent_key=""):
    items = {}
    
    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.update(flatten_data(value, sep=sep, parent_key=new_key))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}{sep}{i}" if parent_key else i
            items.update(flatten_data(item, sep=sep, parent_key=new_key))
    else:
        items[parent_key] = data
        
    return items

if __name__ == "__main__":
    if os.path.exists(INPUT_FILE):
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            nested_data = json.load(file)
        
        flattened_data = flatten_data(nested_data)
        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(flattened_data, file, indent=4)
        
        print(f"Data flattened and saved to {OUTPUT_FILE}")
    else:
        print(f"File {INPUT_FILE} not found.")