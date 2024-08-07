# MULTIPLE INHERITANCE
class Father:
    fname="Manomohan"

class Mother:
    mname="Jayaletchumi"

class Son(Father,Mother):
    name="Kabileshwaran"

kabil=Son()
print(kabil.fname)
print(kabil.mname)
print(kabil.name)