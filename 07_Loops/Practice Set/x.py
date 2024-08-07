'''
Write a program to print multiplication table of n 
using for loop in reversed order
'''
fNum=int(input(" ? X 1 : "))
for i in range(12,0,-1):
    print(f'{fNum} X {i} = {fNum*i}')