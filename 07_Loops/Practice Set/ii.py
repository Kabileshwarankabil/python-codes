'''
Write a program to greet all the person names stored in a list l1 and which starts with 'S' 
l1=["Harry","Soham","Sachin","Rahul"]
'''
l1=["Harry","Soham","Sachin","Rahul"]
# Method 1
for name in l1:
    if(name[0]=='S'):
        print(f'Hello {name}')
# Method 2
for name in l1:
    if name.startswith("S"):
        print(f'Good Morning {name}')




