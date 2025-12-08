# OOPS Program 13: Inner Classes
# Demonstrates nested/inner classes

class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    class Department:
        def __init__(self, dept_name, manager, budget):
            self.dept_name = dept_name
            self.manager = manager
            self.budget = budget
        
        def display_info(self):
            print(f'Department: {self.dept_name}')
            print(f'Manager: {self.manager}')
            print(f'Budget: {self.budget}')
    
    class Employee:
        def __init__(self, emp_id, name, salary):
            self.emp_id = emp_id
            self.name = name
            self.salary = salary
        
        def display_details(self):
            print(f'ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}')
    
    def display_company(self):
        print(f'Company: {self.name}, Location: {self.location}')

if __name__ == '__main__':
    comp = Company('TechCorp', 'Bangalore')
    comp.display_company()
    
    dept = Company.Department('Development', 'Raj Kumar', 500000)
    dept.display_info()
    
    emp = Company.Employee(101, 'Priya Singh', 60000)
    emp.display_details()
