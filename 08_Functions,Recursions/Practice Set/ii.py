'''
Write a python program using function to convert celsius to fahrenheit

F=(C * 9/5) + 32
'''
def celTofahren(c:float)->float:
    return (c * 9/5) + 32

fahrenheit=celTofahren(137)
print(fahrenheit)
