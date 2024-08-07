"""
Repeat program 4 for a list of such words to be censored.
program 4 :- A file contains a word "Donkey" multiple times 
            you need to write a program which replaces 
            this word with ######## by updating the same file.

"""

list=["donkey","monkey","shit","bull shit","dog"]
with open("donkey.txt","r") as f:
    text=f.read()
for i in list:
    text=text.replace(i,"#######")
with open("donkey.txt","w") as f:
    f.write(text)
