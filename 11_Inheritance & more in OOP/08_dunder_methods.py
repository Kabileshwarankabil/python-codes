# class Employee:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,obj):
#         return self.a+ obj.a

# x=Employee(50)
# y=Employee(20)
# print(x+y)


class Calc:
    def __init__(self,x):
        self.x=x
    def __sub__(self,obj):
        return self.x-obj.x
    def __multi__(self,obj):
        return self.x * obj.x
    def __add__(self,obj):
        return self.x+obj.x
    def __div__(self,obj):
        return self.x / obj.x

c1=Calc(10)
c2=Calc(1)
# print(c1+c2)
# print(c1-c2)
print((c1).__div__(c2))
print((c1).__multi__(c2))
print((c1).__add__(c2))
print((c1).__sub__(c2))