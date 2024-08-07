# Find the greater number entered by the user
n1=int(input("Enter 1st Number : "))
n2=int(input("Enter 2nd Number : "))
n3=int(input("Enter 3rd Number : "))
n4=int(input("Enter 4th Number : "))
if(n1>n2 and n1>n3 and n1>n4):
    print(f'{n1} is the greatest number in this list')
elif(n2>n1 and n2>n3 and n2>n4):
    print(f'{n2} is the greatest number in this list')
elif(n3>n1 and n3>n2 and n3>n4):
    print(f'{n3} is the greatest number in this list')
else:
    print(f'{n4} is the greatest number in this list')



    