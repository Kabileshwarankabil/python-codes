"""
Write a program to make a copy of a text file "this.txt"
"""
with open("this.txt","r") as f:
    text=f.read()
with open("copyOfthis.txt","w") as f:
    f.write(text)