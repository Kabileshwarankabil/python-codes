# Write a program to calculate the factorial of a given number using for loop
fac=int(input("Enter the Number : "))
factorial=1
for i in range(fac,0,-1):
    factorial*=i
print(f'The Factorial of {fac} : {factorial}')

