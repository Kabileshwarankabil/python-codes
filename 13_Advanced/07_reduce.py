from functools import reduce
sum=lambda x,y:x+y
li=[1,2,3,4,5]
d=reduce(sum,li)
print(d)