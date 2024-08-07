class Father: # base Class / Parent Class
    f_name="Manomohan"
    netWorth=10200000

class Son(Father): # Child class / Derived Class
    name="Kabileshwaran"

kab=Son()
print(kab.name)
print(kab.netWorth)