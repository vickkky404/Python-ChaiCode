# OOPS Program 11: Constructor and Destructor
# Demonstrates __init__ and __del__ concepts

class Student:
    student_count = 0
    
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        Student.student_count += 1
        print(f'Student {self.name} created')
    
    def display_info(self):
        print(f'Name: {self.name}, Roll: {self.roll_no}, Marks: {self.marks}')
    
    def __del__(self):
        print(f'Student {self.name} destroyed')
        Student.student_count -= 1

if __name__ == '__main__':
    s1 = Student('Raj', 101, 85)
    s2 = Student('Priya', 102, 92)
    s1.display_info()
    s2.display_info()
    print(f'Total students: {Student.student_count}')
    del s1
