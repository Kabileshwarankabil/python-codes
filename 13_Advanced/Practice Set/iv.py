"""
Write a program to filter a list of numbers which are divisible by 5
"""
div=lambda x: x%5==0
li=[10,11,20,32,50,43]
d=filter(div,li)
print(list(d))
