try:
    n=int(input("1 :"))
    n1=int(input("2 :"))
    if n1>n:
        raise Exception("This is too Big Value")
    print(n/n1)
except Exception as e:
    print(f'The Error : {e}')