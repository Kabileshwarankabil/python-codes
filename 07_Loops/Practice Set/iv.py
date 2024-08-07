# Write a program to find whether a given number is prime or not
numb=int(input("Enter a Number : "))
k=0
for i in range(1,numb):
    if(numb%i==0):
        k+=1
if(k==1):
    print(f'{numb} is a Prime Number ')
else:
    print(f'{numb} is not a Prime Number ')
    
