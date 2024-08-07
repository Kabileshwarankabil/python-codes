#Favourite languages of 4 friends
f1=input("Kabil's Favourite Language: ")
f2=input("Dhanush's Favourite Language: ")
f3=input("Visura's Favourite Language: ")
f4=input("Harish Kumar's Favourite Language: ")
FavLang={
    "Kabil":f1,
    "Dhanush":f2,
    "Visura":f3,
    "Harish Kumar":f4
}
for key, value in FavLang.items():
    print(key,":=>",value)