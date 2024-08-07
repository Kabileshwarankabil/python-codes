class GrandParent:
    age1=89

class Parent(GrandParent):
    age2=50

class Child(Parent):
    age3=21

cL1=Child()
print(cL1.age1)
print(cL1.age2)
print(cL1.age3)