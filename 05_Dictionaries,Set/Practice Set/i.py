tamilDictionary={
    "Mannippu":"Forgiving",
    "Amma":"Mother",
    "Appa":"Father",
    "Thambi":"Younger Brother",
    "Anna":"Elder Brother",
    "Maama":"Uncle",
    "Thaatha":"GrandFather"
}
print(tamilDictionary.keys())
selword=input("Select a word to know English translation: ")
val=tamilDictionary.get(selword)
if val==None:
    print("Not Found")
else:
    print(val)
