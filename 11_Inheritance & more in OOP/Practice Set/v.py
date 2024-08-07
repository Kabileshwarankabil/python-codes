"""
Write a class vector representing a vector of n dimension.
overload the + and * operator which calculates the sum and the dot product of them
"""
class Vector2D:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,obj):
        return complex(self.a + obj.a,self.b + obj.b)
    def __multi__(self,obj):
        return complex((self.a*obj.a - obj.b*self.b),(self.a*obj.b + obj.a*self.b))
    
v1=Vector2D(2,3)
v2=Vector2D(2,3)
v3=(v1).__add__(v2)
v4=(v1).__multi__(v2)
print(v3)
print(v4)
