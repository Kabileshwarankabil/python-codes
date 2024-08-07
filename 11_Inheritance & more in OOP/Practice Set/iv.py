"""
Write a class complex to represent complex numbers 
along with overloaded operators + and * which adds and multiples them
"""

class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,obj):
        return Complex(self.a + obj.a,self.b + obj.b)
    def __multi__(self,obj):
        return Complex((self.a * obj.a)-(obj.b *self.b),(self.a*obj.b)+(obj.a*self.b))

c1=Complex(2,5)
c2=Complex(3,4)
c3=c1+c2
print(c3.a,c3.b)
c4=(c1).__multi__(c2)
print(c4.a,c4.b)