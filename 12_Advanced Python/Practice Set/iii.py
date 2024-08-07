"""
Write a list comprehension to print a list 
which contains the multiplication table of a user entered number.
"""
n=int(input("Enter the Number :"))
list1=[n*i for i in range(1,13)]
print(list1)