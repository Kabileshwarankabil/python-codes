class Employee:
    a=10
    b=20
    c=30
    @classmethod
    def setAttribute(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c

emp1=Employee()
print(Employee.a)
print(Employee.b)
print(Employee.c)
emp1.setAttribute(2,4,6)
print(Employee.a)
print(Employee.b)
print(Employee.c)

