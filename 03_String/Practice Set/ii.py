name=input("Name : ")
date=input("Date : ")

template='''Dear \t<name>
\t You are Selected to Bsc Computer Science Course in 
\t Trincomalee campus 
\t <date>
'''
print(template.replace("<name>",name).replace("<date>",date))