try:
    n1=int(input("Enter First Number : "))
    n2=int(input("Enter Second Number: "))
    print(f'The Multiplication :{n1*n2}')
    print(f'The Sum : {n1+n2}')
    print(f'The Division :{n1/n2}')
except ValueError: # Value Error
    print("ValueError Occured!")
except ZeroDivisionError:
    print("You Can't Divide a Number by 0 ")
except Exception as e: # For Other Errors
    print(f'The Error : {e}')

print("Program Executed Successful!")
