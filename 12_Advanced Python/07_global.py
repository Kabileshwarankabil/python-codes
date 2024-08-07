a=9
def funct():
    global a # modifies the global a 
    a=10
    print(a)
    a=100
    print(a)

print(a) # Before Calling the function
funct() # calling the function
print(a) # After Calling the function
"""
Expected Output
    9
    10
    100
    100
"""