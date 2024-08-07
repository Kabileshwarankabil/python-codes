"""
Write a class calculate capable of finding square , cube and square root of a number
"""
import math
class Calculator:
    def __init__(self,number):
        self.number=number

    def square(self):
        return self.number**2
    def cube(self):
        return self.number**3
    def squareRoot(self):
        return math.sqrt(self.number)

n1=Calculator(9)
print(n1.square())
print(n1.cube())
print(n1.squareRoot())
