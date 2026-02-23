"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time

while True:
    try:
        seconds = int(input("Enter the number of seconds for the timer: "))
        if seconds < 0:
            print("Please enter a non-negative integer.")
            continue
        break        
    except ValueError:
        print("Please enter a valid integer for the timer.")
        continue

print(f"Timer started for {seconds} seconds.")
for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02d}:{secs:02d}"
    print(f"Time remaining: {time_format}", end='\r')
    time.sleep(1)
print("\nTime's up! \a")  # Beep sound if supported by the terminal
