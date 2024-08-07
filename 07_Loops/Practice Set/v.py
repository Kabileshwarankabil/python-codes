# Write a program to find the sum of first n natural numbers using while loop
fNumb=int(input("First Number : "))
lNumb=int(input("Last Number : "))
sum=0
i=fNumb
while i<=lNumb:
    sum+=i
    i+=1

print(f'The Sum ({fNumb} - {lNumb}) : {sum}')
