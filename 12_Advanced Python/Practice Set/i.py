"""
Write a program to open three files 1.txt, 2.txt and 3.txt. 
If any of these files are not present , 
a message without existing the program must be printed prompting the same
"""
try:
    with open("1.txt","r") as f:
        pass
    with open("2.txt","r") as f:
        pass
    with open("3.txt","r") as f:
        pass
except Exception as e:
    print(f"Not Found {e}")
