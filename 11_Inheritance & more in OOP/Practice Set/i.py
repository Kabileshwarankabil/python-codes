"""
Create a class 2-d vector and
use it it to create another class representing a 3-d vector
"""
class Vector2D:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def display(self):
        print(f'{self.i}i + {self.j}j')

class Vector3D(Vector2D):
    def __init__(self,i,j,k):
        self.k=k
        super().__init__(i,j)
    def display(self):
        print(f'{self.i}i + {self.j}j + {self.k}k')

v2=Vector2D(2,3)
v3=Vector3D(3,8,8)
v2.display()
v3.display()