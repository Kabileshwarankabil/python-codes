# Write a program to print multiplication table of a given number using for loop
fNum=int(input(" ? X 1 : "))
lNum=int(input(f'{fNum} X ? : '))
print('\n------------------------------\n')
for i in range(1,lNum+1):
    print(f'{fNum} X {i} = {fNum*i}')

print('\n------------------------------')