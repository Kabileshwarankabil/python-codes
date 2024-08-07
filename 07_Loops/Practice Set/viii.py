'''
Write a program to print the following star pattern
*
* *
* * *
'''
for i in range(1,4):
    for j in range(i):
        print('*',end=' ')
    print(' ')