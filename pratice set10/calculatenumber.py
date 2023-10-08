class Calculator:
    def __init__(self,num):
        self.numbers = num
    def square(self):
        print(f"The value of {self.numbers} square is {self.numbers **2}")
    def squareRoot(self):
         print(f"The value of {self.numbers} squareRoot is {self.numbers **0.5}")
    def cube (self):
         print(f"The value of {self.numbers} cube is {self.numbers **3}")

a = Calculator(3 )
a.square()  
a.squareRoot()
a.cube()  