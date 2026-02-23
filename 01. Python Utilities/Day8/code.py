"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import string
import random
import getpass

issues = []
def check_password_strength(password):
    if len(password) < 8:
        issues.append("Password is too short (Minimum 8 characters).")
    if not any(c.islower() for c in password):
        issues.append("Missing lower case latter")
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case latter")
    if not any(c.isdigit() for c in password):
        issues.append("Missing digit in password")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing a special latter in password")
    return issues

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars)for _ in range(length))

password = getpass.getpass("Enter a password : ")
check_password_strength(password)

if not issues:
    print("Strong password! you are good to go.")
else:
    print("Your got week password!")
    for i in issues:
        print(f"{i}")
    
    suggestion = generate_strong_password()
    print(f"Suggested strong password: {suggestion}")


        