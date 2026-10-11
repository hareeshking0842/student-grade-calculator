
# Student Grade Calculator

name = input("Enter student name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))
mark4 = float(input("Enter mark for Subject 4: "))
mark5 = float(input("Enter mark for Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

if min(mark1, mark2, mark3, mark4, mark5) < 0 or max(mark1, mark2, mark3, mark4, mark5) > 100:
    print("Invalid marks! Enter marks from 0 to 100.")
else:
    print("\n--- STUDENT RESULT ---")
    print("Name:", name)
    print("Total:", total, "/ 500")
    print("Average:", average)

    if min(mark1, mark2, mark3, mark4, mark5) < 35:
        grade = "F"
        status = "Fail"
    elif average >= 90:
        grade = "A"
        status = "Pass"
    elif average >= 75:
        grade = "B"
        status = "Pass"
    elif average >= 60:
        grade = "C"
        status = "Pass"
    else:
        grade = "D"
        status = "Pass"

    print("Grade:", grade)
    print("Result:", status)
  
