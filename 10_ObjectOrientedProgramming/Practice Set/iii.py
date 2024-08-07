"""
Create a class with a class attribute a ; 
create an object from it and set a directly using object . 
a=0. does this change the class attribute?
"""
class New:
    a=10
    def printf(self):
        print(self.a)

demo=New()
demo.a=0

demo.printf()