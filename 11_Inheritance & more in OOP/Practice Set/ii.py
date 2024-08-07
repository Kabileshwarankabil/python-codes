"""
Create a class pets from a class Animals 
and further create class Dog from Pets. Add a method bark to class Dog
"""
class Animal:
    pass
class Pets(Animal):
    pass
class Dog(Pets):
    def bark(self):
        return "Bow-Bow"
    
d1=Dog()
print(d1.bark())