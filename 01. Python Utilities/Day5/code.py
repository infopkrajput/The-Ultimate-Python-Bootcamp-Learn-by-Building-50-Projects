"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

def add_emojis(message):
    emoji_dict = {
        "happy": "😊",
        "love": "❤️",
        "code": "💻",
        "tea": "🍵"
    }
    
    updated_words = []
    
    for word in message.split():
      cleaned = word.lower().strip(".!?%,")
      emoji = emoji_dict.get(cleaned,"")
      if emoji:
        updated_words.append(f"{word} {emoji} ")
      else:
        updated_words.append(f"{word} ")
    
    updated_message = "".join(updated_words)
    return updated_message
    

message = input("Enter your message: ")
print(add_emojis(message))

