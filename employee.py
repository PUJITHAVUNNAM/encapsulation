class Employee:
    def __init__(self, salary):
        self.__salary = salary
        self.__logs = []

    def get_salary(self):
        self.__logs.append("Salary access attempted")
        return self.__salary

    def update_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("Salary updated successfully")
        else:
            print("Salary cannot be decreased")

emp = Employee(30000)

print("Salary:", emp.get_salary())

emp.update_salary(40000)
print("Updated Salary:", emp.get_salary())

emp.update_salary(25000)

print(emp.__dict__)