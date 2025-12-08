# OOPS Program 26: Magic Methods for Comparison
# Demonstrates __eq__, __lt__, __gt__, __le__, __ge__, __ne__

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def __eq__(self, other):
        return self.gpa == other.gpa
    
    def __lt__(self, other):
        return self.gpa < other.gpa
    
    def __gt__(self, other):
        return self.gpa > other.gpa
    
    def __le__(self, other):
        return self.gpa <= other.gpa
    
    def __ge__(self, other):
        return self.gpa >= other.gpa
    
    def __ne__(self, other):
        return self.gpa != other.gpa
    
    def __repr__(self):
        return f'Student({self.name}, {self.gpa})'

if __name__ == '__main__':
    s1 = Student('Raj', 3.8)
    s2 = Student('Priya', 3.9)
    s3 = Student('Arjun', 3.8)
    
    print('s1 == s3:', s1 == s3)
    print('s1 < s2:', s1 < s2)
    print('s2 > s1:', s2 > s1)
    print('s1 != s2:', s1 != s2)
    
    students = [s2, s1, s3]
    students.sort()
    print('Sorted:', students)
