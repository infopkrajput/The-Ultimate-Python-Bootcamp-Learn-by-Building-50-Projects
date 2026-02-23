"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime
name = input("What is your name ? ").strip()
age = input("How old are you ? ").strip()
city = input("What is your city name ? ").strip()
profession = input("What is your profession ? ").strip()
hobby = input("What is your hobby ? ").strip()

date = datetime.date.today().isoformat()
star = "*" * 80

print(f"{star}\nHello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and i absolutely enjoy {hobby} in my free time. Nice to meet you!\n\nLogged on: {date}\n{star}")