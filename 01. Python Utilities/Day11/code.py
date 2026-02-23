"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

def calculate_compatibility(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0 
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')
    
    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    
    return min(score, 100)

def run_friendship_calculator():
    print("Welcome to the Friendship Compatibility Calculator! 🌟")
    name1 = input("Enter the name of Friend A: ")
    name2 = input("Enter the name of Friend B: ")
    
    score = calculate_compatibility(name1, name2)
    
    if score >= 80:
        message = "You're like chai and samosa — made for each other! ❤️"
    elif score >= 50:
        message = "You have a good bond, keep nurturing it! 😊"
    else:
        message = "Well... opposites attract, maybe? 🤔"
    
    print("\n" + "="*40)
    print(f"{'Compatibility Score: ' + str(score) + '%':^40}")
    print(f"{message:^40}")
    print("="*40)    
    
if __name__ == "__main__":
    run_friendship_calculator()
    