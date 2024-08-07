marks=[]
mark1=int(input("Marks-1 :"))
mark2=int(input("Marks-2 :"))
mark3=int(input("Marks-3 :"))
mark4=int(input("Marks- 4:"))
mark5=int(input("Marks-5 :"))
mark6=int(input("Marks- 6:"))

marks.extend([mark1,mark2,mark3,mark4,mark5,mark6])
marks.sort()
print(marks)