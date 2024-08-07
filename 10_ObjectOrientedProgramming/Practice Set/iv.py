"""
Add a static method in problem 2 to geet the user with hello
"""
class Calculation:
    def __init__(self,number):
        self.number=number

    def square(self):
        return self.number**2
    def cube(self):
        return self.number**3
    def squareRoot(self):
        return self.number**(1/2)
    
    @staticmethod
    def greet():
        print("Hello")

n1=Calculation(9)
print(n1.square())
print(n1.cube())
print(n1.squareRoot())

n1.greet()
