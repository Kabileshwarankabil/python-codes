"""
Write __str__() method to print the vector as follows:
7i + 8j +10k
assume vector of dimension 3 for this problem
"""
class Vector3D:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f'{self.i}i {self.j}j {self.k}k'

v=Vector3D(2,4,7)
print(v)