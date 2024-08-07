"""
A file contains a word "Donkey" multiple times 
you need to write a program which replaces this word with ######## by updating the same file.
"""
with open("donkey.txt","r") as f:
    text=f.read()
text=text.replace('donkey','######')
with open("donkey.txt","w") as f:
    f.write(text)
    