# Write a program to print multiplication table of a given number using while loop
fNum=int(input(" ? X 1 : "))
lNum=int(input(f'{fNum} X ? : '))
i=1
print('\n------------------------------\n')
while i<=lNum:
    print(f'{fNum} X {i} = {fNum*i}')
    i+=1
print('\n------------------------------')