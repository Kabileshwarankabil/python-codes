def func():
    try:
        a=int(input("Enter the 1st Number  :"))
        b=int(input("Enter the 2nd Number  :"))
        print(a/b)
        return a/b
    except Exception as e:
        print(f'The error is {e}')
        return 0
    finally: # This runs always even inside a function
        print("I Will Always Run")

func()