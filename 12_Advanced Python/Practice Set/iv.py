"""
Write a program to display a/b where a and b are integers.
If b=0, display infinite by handling the ZeroDivisionError
"""
try:
    a=int(input("a: "))
    b=int(input("b: "))
    print(a/b)
except ZeroDivisionError:
    print("This is : ZeroDivisionError ")
except Exception as e:
    print(f"This is : {e}")