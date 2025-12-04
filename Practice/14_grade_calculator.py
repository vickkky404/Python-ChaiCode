# Grade Calculator

def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

marks = float(input("Enter marks (0-100): "))
if 0 <= marks <= 100:
    grade = get_grade(marks)
    print(f"Marks: {marks}, Grade: {grade}")
else:
    print("Invalid marks! Enter between 0-100")
