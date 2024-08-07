'''
Write a program to print the following star pattern
  *
 ***
*****
'''
for i in range(1,4):
    for j in range(3-i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    for j in range(3-i):
        print(' ',end='')
    print('\n',end='')
