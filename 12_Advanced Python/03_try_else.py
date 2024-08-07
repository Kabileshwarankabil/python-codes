try:
    a=int(input("Number-1 : "))
    b=int(input("Number-2 : "))
    print(f'The Addition : {a+b}')
except Exception as e:
    print(f'The Error Is : {e}')
else: # Runs If only try block is successful
    print("Try is Successful!")