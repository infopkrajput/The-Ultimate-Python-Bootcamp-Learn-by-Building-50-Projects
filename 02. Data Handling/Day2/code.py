"""
Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_student_data():
    student = {}
    
    while True:
        name = input("Enter student name: ").strip()
        
        if name.lower() == 'done':
            break
        if name in student:
            print("Student already exists. Please enter a unique name.")
            continue
        
        try:
            marks = float(input(f"Enter marks for {name}: "))
            student[name] = marks
        except ValueError:
            print("Invalid input. Please enter a number for marks.")
            
    return student

def display_report(student):
    
    if not student:
        print("No student data to display.")
        return
    
    total_students = len(student)
    average_marks = sum(student.values()) / total_students
    highest_marks = max(student.values())
    lowest_marks = min(student.values())
    
    highest_scorers = [name for name, marks in student.items() if marks == highest_marks]
    lowest_scorers = [name for name, marks in student.items() if marks == lowest_marks]
    
    print("\nStudent Marks Report")
    print("-" * 20)
    print(f"Total Students: {total_students}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Highest Marks: {highest_marks} - {', '.join(highest_scorers)}")
    print(f"Lowest Marks: {lowest_marks} - {', '.join(lowest_scorers)}")
    print("-" * 20)
    print("Detailed Student Marks:")
    for name, marks in student.items():
        print(f"{name}: {marks}")
        
def main():
    print("Welcome to the Student Marks Analyzer!")
    print("Enter student names and their marks. Type 'done' when finished.")
    
    student_data = collect_student_data()
    display_report(student_data)

if __name__ == "__main__":
    main()