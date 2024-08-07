a=True
b=False
print(a and b)#False
print(a or b)#True
print(not a)#False
print(not b)#True

age=17
nationality="sri lankan"
nation=nationality.capitalize()
if(age>=18 and nation=="Sri lankan"):
    print("You are eligible to vote")
elif(age<18 and nation=="Sri lankan"):
    print("You are not an adult to Vote")
    print(f'You have to wait {18-age} more years to vote')
else:
    print("Sorry You are not a Sri lankan to vote")