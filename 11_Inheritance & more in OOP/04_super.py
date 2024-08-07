# Super method is used to access the methods of a super class in the derived class
class GrandParent:
    age1=89
    def __init__(self):
        print("GrandParent")

class Parent(GrandParent):
    age2=56
    def __init__(self):
        print("Parent")
        super().__init__()

class Child(Parent):
    age3=25
    def __init__(self):
        super().__init__()
        print("Child")

c1=Child()