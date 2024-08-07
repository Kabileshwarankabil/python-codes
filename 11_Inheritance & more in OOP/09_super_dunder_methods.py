class Employee:
    def __init__(self,a,name):
        self.a=a
        self.name=name
    def __str__(self):
        return self.name
    def __len__(self):
        return self.a


c1=Employee(40,"Kabil")
c2=Employee(50,"Dhanu")
print(c1,c2)
print(str(c1))
print(str(c2))
print(len(c1))