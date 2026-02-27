"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64
import os

VAULT_FILE = "vault.txt"

def encode_data(data):
    return base64.b64encode(data.encode("utf-8")).decode("utf-8")

def decode_data(data):
    return base64.b64decode(data.encode("utf-8")).decode("utf-8")

def rate_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    sum_score = sum([length >= 8, has_upper, has_lower, has_digit, has_special])
    
    if sum_score <= 2:
        return "Weak"
    elif sum_score == 3:
        return "Medium"
    else:
        return "Strong"
    

def add_credentials():
    website = input("Enter Website: ").strip()
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    strength = rate_password_strength(password)
    print(f"Password Strength: {strength}")
    credentials = f"{website}|{username}|{password}"
    encoded_credentials = encode_data(credentials)
    with open(VAULT_FILE, "a", encoding="utf-8") as file:
        file.write(encoded_credentials + "\n")
    print("Credentials added successfully.")    

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("No credentials found.")
        return
    
    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    print("\nSaved Credentials:")
    for line in lines:
        decoded_line = decode_data(line.strip())
        website, username, password = decoded_line.split("|")
        masked_password = "*" * len(password)
        print(f"Website: {website}, Username: {username}, Password: {masked_password}")

def update_password():
    if os.path.exists(VAULT_FILE):
        website_to_update = input("Enter the website for which you want to update the password: ").strip()
        new_password = input("Enter the new password: ").strip()
        strength = rate_password_strength(new_password)
        print(f"Password Strength: {strength}")
        
        with open(VAULT_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        updated_lines = []
        found = False
        for line in lines:
            decoded_line = decode_data(line.strip())
            website, username, _ = decoded_line.split("|")
            if website == website_to_update:
                updated_credentials = f"{website}|{username}|{new_password}"
                updated_lines.append(encode_data(updated_credentials) + "\n")
                found = True
            else:
                updated_lines.append(line)
        
        if found:
            with open(VAULT_FILE, "w", encoding="utf-8") as file:
                file.writelines(updated_lines)
            print("Password updated successfully.")
        else:
            print("Website not found.")

def main():
    while True:
        print("\nOffline Credential Manager")
        print("1. Add Credentials")
        print("2. View Credentials")
        print("3. Update Password")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_credentials()
        elif choice == "2":
            view_credentials()
        elif choice == "3":
            update_password()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()