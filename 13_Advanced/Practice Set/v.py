"""
Write a program to find the maximum of the numbers in a list using the reduce function
"""
from functools import reduce
def max(x,y):
    if(x>y):
        return x
    else:
        return y
li=[12,43,65,34,76]
print(reduce(max,li))
