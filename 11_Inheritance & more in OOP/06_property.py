class Employee:
    a=10
    b=20
    c=30
    @classmethod
    def setAttribute(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c
    @property
    def length(self):
        return self.a

emp1=Employee()
emp1.setAttribute(1,2,3)
# print(Employee.a)
# print(Employee.b)
# print(Employee.c)
print(emp1.length) # prooperty method