'''
Write a program using function to find greatest of three numbers
'''
'''
def max(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    elif(b>a):
        if(b>c):
            return b
        else:
            return c
    elif(c>a):
        if(c>b):
            return c
        else:
            return b

print(max(910,210,30))
'''
def max(n1,n2,n3):
    if(n1>n2):
        greater=n1
    else:
        greater=n2
    if(n3>greater):
        greater=n3
    return greater

a=max(110,290,30)
print(a)
