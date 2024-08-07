"""
Write a program to find out the line number where python is present from question 6
"""
with open("mine.log","r") as f:
    text=''
    cond='python' in text
    l=0
    while not(cond):
        text=f.readline()
        l+=1
        cond='python' in text
    
print(f'Found in {l} line')