class Person:
    country ="Nepal"

    def __init__(self):
        print("Intializing person..\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Intializing Employee..\n")

    def getSalary(self):
        print(f"Salary is {self.Salary}")        


    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am Luckily breathing...")


class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Intializing Programmer..\n")


    def getSalary(self):
        print(f"No salary to programmer")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer so I am Luckily breathing...")
    

# p =Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer() 
pr.takeBreath()



