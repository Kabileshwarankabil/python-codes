'''
Write a recursive function 
to calculate the sum of first n natural numbers
'''
def sumOfNatural(n):
    if(n==1):
        return 1
    return n+sumOfNatural(n-1)

number=sumOfNatural(10)
print(number)