class Employee:
    a=10
    @classmethod
    def setAttribute(cls,a):
        cls.a=a
    @property
    def length(self):
        return self.a
    @length.setter
    def length(self,value):
        self.a=value

emp=Employee()
emp.setAttribute(2)
emp.length=100
print(emp.length)
