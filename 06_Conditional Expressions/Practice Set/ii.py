'''
Write a program to find out whether a student is pass or fail 
    if it requires total 40% and at least 33% in each subject to pass. 
    Assume 3 subjects and take marks as an input from the user
'''
# total >= 40%
# >= 33% in each subject
subMark1=int(input("Marks for Mathematics: ")) 
subMark2=int(input("Marks for Computing: "))
subMark3=int(input("Marks for Bussiness Studies: "))

total=subMark1+subMark2+subMark3
avetotal=total/3
#Testing
print(avetotal)

#condition
if(avetotal>=40 and (subMark1>=33 and subMark2>=33 and subMark3>=33)):
    print("Pass")
else:
    print("Fail")
