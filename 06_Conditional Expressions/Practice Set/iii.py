'''
A spam comment is defined as a text containing following keywords:
"make a lot of money", "buy now", "subscribe this", "click this".
write a program to detect these spams.
'''
spamComment1="make a lot of money"
spamComment2="buy now"
spamComment3="subscribe this"
spamComment4="click this"
email=input("Enter a comment : ").lower()
spam=False
if('make a lot of money' in email):
    spam=True
if('buy now' in email):
    spam=True
if('subscribe this' in email):
    spam=True
if('click this' in email):
    spam=True

print("Spam is : ",spam)
