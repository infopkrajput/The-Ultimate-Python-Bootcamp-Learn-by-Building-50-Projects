"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
"""
 
import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return Fernet(key_file.read())
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return Fernet(key)
    
key = load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        print("No vault found. Starting with an empty vault.")
        return []
    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    

def save_vault(data):
    with open(VAULT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    encrypted_content = key.encrypt(content.encode()).decode()
    
    data = load_vault()
    
    data.append({
        "title": title,
        "content": encrypted_content,
        "timestamp": timestamp
    })
        
    save_vault(data)
    print("Note added successfully.")
    
def list_notes():
    data = load_vault()
    if not data:
        print("No notes found.")
        return
    
    for idx, note in enumerate(data, 1):
        print(f"{idx}. {note['title']} (Created on: {note['timestamp']})")
        
def view_note():
    data = load_vault()
    if not data:
        print("No notes found.")
        return
    
    list_notes()
    
    try:
        choice = int(input("Enter note number to view: "))
        if 1 <= choice <= len(data):
            note = data[choice - 1]
            decrypted_content = key.decrypt(note["content"].encode()).decode()
            print(f"Title: {note['title']}")
            print(f"Content: {decrypted_content}")
            print(f"Created on: {note['timestamp']}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
def search_notes():
    keyword = input("Enter keyword to search: ").strip().lower()
    data = load_vault()
    found = False
    for note in data:
        if keyword in note["title"].lower() or keyword in note["content"].lower():
            print(f"Title: {note['title']}, Created on: {note['timestamp']}")
            found = True
    if not found:
        print("No matching notes found.")

def main():
    while True:
        print("\n--- Notes Locker ---")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")
        
        try:
            choice = int(input("Choose an option: ").strip())
            match choice:
                case 1:
                    add_note()
                case 2:
                    list_notes()
                case 3:
                    view_note()
                case 4:
                    search_notes()
                case 5:
                    print("Exiting Notes Locker. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nExiting Notes Locker. Goodbye!")
            break
        
if __name__ == "__main__":
    main()
    