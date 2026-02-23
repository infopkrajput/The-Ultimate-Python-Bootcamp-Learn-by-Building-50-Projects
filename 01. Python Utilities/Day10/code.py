"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

def caesar_cipher(message, key, mode='encrypt'):
    result = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            if mode == 'encrypt':
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

while True:
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
    if choice in ['E', 'D']:
        break
    else:
        print("Please enter 'E' for encrypt or 'D' for decrypt.")
message = input("Enter the message: ")
while True:    
    try:
        key = int(input("Enter the numeric secret key: "))
        break
    except ValueError:
        print("Please enter a valid integer for the key.")
if choice == 'E':
    encrypted_message = caesar_cipher(message, key, mode='encrypt')
    print(f"Encrypted Message: {encrypted_message}")
else:
    decrypted_message = caesar_cipher(message, key, mode='decrypt')
    print(f"Decrypted Message: {decrypted_message}")

