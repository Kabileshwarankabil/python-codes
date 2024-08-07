"""
Store the multiplication table generated in problem 3 
in a file named Tables.txt
"""
n=int(input("Enter the Number : "))
list1=[n*i for i in range(1,13)]
with open("Tables.txt","w") as f:
    f.write(str(list1))