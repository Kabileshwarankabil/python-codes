'''
Write a python function 
to print multiplication table of a given number
'''
def multitable(n):
    print("___________________")
    for i in range(1,13):
        print(f'| {n} X {i} => {n*i} |')
    print("___________________")

n=int(input("Enter the Number : "))
multitable(n)