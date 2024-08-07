def function():
    try:
        n=int(input("1st :"))
        n1=int(input("2nd :"))
        print(n+n1)
    except Exception as e:
        print(f'The Error is : {e}')
    finally:
        print("###########################")

print(__name__)
if __name__=='__main__':
    function()
    print("Completed")
