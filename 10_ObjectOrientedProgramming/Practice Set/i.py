"""
Create a class programmer 
for storing information of few programmers working at microsoft
"""
class Programmer:
    company="microsoft"
    def __init__(self,name,work):
        self.name=name
        self.work=work

    def printDetails(self):
        print(f'{self.name} ')
        print(f'Works at {self.company} ')
        print(f'Works as {self.work} ')
        print(f'\n--------------------------\n')

pro1=Programmer("Jimmy","AI Engineer")
pro2=Programmer("Karthick","Software Engineer")
pro3=Programmer("Abdul Bari","Senior Developer")
pro4=Programmer("Sathya Nadel","Chief Execute Officer")

pro1.printDetails()
pro2.printDetails()
pro3.printDetails()
pro4.printDetails()