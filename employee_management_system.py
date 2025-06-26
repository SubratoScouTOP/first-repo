class EmployeeManagementSystem:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department
    def get_name(self):
        return self.name
    def get_emp_id(self):
        return self.emp_id
    def get_salary(self):
        return self.salary
    def get_department(self):
        return self.department
    def set_name(self, name):
        self.name = name
    def set_emp_id(self, emp_id):
        self.emp_id = emp_id
    def set_salary(self, salary):
        self.salary = salary
    def set_department(self, department):
        self.department = department
    def display_employee_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
        print("-" * 30)
print("Welcome to the Employee Management System")
emp1 = EmployeeManagementSystem("Ravi Kumar", "E001", 40000, "HR")
emp1.display_employee_info()
emp2 = EmployeeManagementSystem("Sita Sharma", "E002", 55000, "IT")
emp2.display_employee_info()
emp3 = EmployeeManagementSystem("Amit Verma", "E003", 47000, "Finance")
emp3.display_employee_info()
emp4 = EmployeeManagementSystem("Neha Joshi", "E004", 60000, "Marketing")
emp4.display_employee_info()
