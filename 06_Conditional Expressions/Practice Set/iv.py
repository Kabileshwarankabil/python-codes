'''
write a program to find whether a given username 
contains less then 10 characters or not
'''
username=input("Enter a username : ")
if(len(username)<10):
    print("This is not a strong username ")
else:
    print("This is a strong username ")