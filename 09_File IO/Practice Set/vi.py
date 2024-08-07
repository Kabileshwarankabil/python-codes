"""
Write a program to mine a log file and find out whether it contains 'python'
"""
with open("mine.log","r") as f:
    text=f.read()
if("python" in text):
    print("Found")
else:
    print("Not Found")