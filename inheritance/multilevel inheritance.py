class Person:
    country ="Nepal"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.Salary}")        


    def takeBreath(self):
        print("I am an Employee so I am Luckily breathing...")


class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmer")

    def takeBreath(self):
        print("I am an Programmer so I am Luckily breathing...")
    

p =Person()
print(p.country)
p.takeBreath()
# print(p.company) # throws an error
e = Employee()
e.takeBreath()
print(e.company) 
pr = Programmer() 
print(pr.company)
pr.takeBreath()



