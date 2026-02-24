"""
Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os

FILENAME = 'contacts.csv'

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone","Email"])
        
def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    
    with open(FILENAME,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists!")
                return
    
    with open(FILENAME,"a",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
        print("Contact added.")
        
def view_contacts():
    with open(FILENAME,"r",encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        if len(rows) <= 1:
            print("No contacts found.")
            return
        
        print("Your Contacts: \n")
        print(f"{rows[0][0]:<20} {rows[0][1]:<15} {rows[0][2]:<30}")
        print("-" * 65)
        for row in rows[1:]:
            print(f"{row[0]:<20} {row[1]:<15} {row[2]:<30}")
        print("-" * 65)
            
def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False
    
    with open(FILENAME,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if search_name in row["Name"].lower():
                print(f"{row['Name']:<20} {row['Phone']:<15} {row['Email']:<30}")
                found = True
        if not found:
            print("No contacts found.")
            
def main():
    while True:
        print("\n1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
