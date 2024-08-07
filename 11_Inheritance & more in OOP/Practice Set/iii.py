"""
Create a class Employee and add salary and increment properties to it.
Write a method salaryAfterIncrement method with a @property decorator 
with a setter which changes the value of increment based on the salary
"""
class Employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    @property
    def salaryAfterIncrement(self):
        return self.salary * (1+self.increment)
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self):
        self.salary=self.salary*(1+ self.increment)

em1=Employee(10000,0.5)
em1.salaryAfterIncrement=1200
print(em1.salaryAfterIncrement)
