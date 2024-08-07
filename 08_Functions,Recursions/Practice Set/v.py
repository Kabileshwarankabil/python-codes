'''
Write a python function to print first n lines of the following pattern:

* * *
* *
*
     for n=3
'''
def drawPattern(n):
    for j in range(n,0,-1):
        print('*'*j)

drawPattern(5)