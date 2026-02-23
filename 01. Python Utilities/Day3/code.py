"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

star = "*" * 50
persons = int(input("Enter how many persons you are ? "))

names = []
for i in range(persons):
    name = input(f"Enter the name of person {i+1} : ")
    names.append(name)
    
total_bill_amount = float(input("Enter total bill amount : "))
share_of_bill = round(total_bill_amount/persons,2)

print(f"{star}\nTotal number of persons are : {persons}\nTotal bill amount is : ₹{total_bill_amount}\nEach person owes : ₹{share_of_bill}\n")

for name in names:
    print(f"{name} owes ₹{share_of_bill}")
print(star)