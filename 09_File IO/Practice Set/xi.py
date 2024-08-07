"""
Write a python program to rename a file to "renames_by_python".txt
"""
import os
oldname=input("Enter the file name to rename: ")
newname=input("Enter the New Name to the file : ")
with open(oldname,"r") as f:
    text=f.read()
with open(newname,"w") as f:
    f.write(text)
os.remove(oldname)