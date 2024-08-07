"""
Write a program to find out 
whether a file is identical & matches the content of another file
"""
with open("this.txt","r") as f:
    text=f.read()
with open("copyOfthis.txt","r") as f:
    text1=f.read()
if(text==text1):
    print("Identical ")
else:
    print("Not Identical")