# #get 8 numbers from user and display unique numbers from it
# print("Enter 8 Numbers :")
# n1=int(input("#1 :"))
# n2=int(input("#2 :"))
# n3=int(input("#3 :"))
# n4=int(input("#4 :"))
# n5=int(input("#5 :"))
# n6=int(input("#6 :"))
# n7=int(input("#7 :"))
# n8=int(input("#8 :"))

# numSet={n1,n2,n3,n4,n5,n6,n7,n8}
# print(numSet)

# Method 2
# print("Enter 8 Numbers :")
# Inputs from users 
n1=int(input("#1 :"))
n2=int(input("#2 :"))
n3=int(input("#3 :"))
n4=int(input("#4 :"))
n5=int(input("#5 :"))
n6=int(input("#6 :"))
n7=int(input("#7 :"))
n8=int(input("#8 :"))
numSet=set()

numSet.add(n1)
numSet.add(n2)
numSet.add(n3)
numSet.add(n4)
numSet.add(n5)
numSet.add(n6)
numSet.add(n7)
numSet.add(n8)

print(numSet)