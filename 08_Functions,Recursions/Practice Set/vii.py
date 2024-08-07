'''
Write a python function 
to remove a given word from a list and strip it at the same time
'''
def removeWord(wordList,word):
    word=word.strip()
    if(word in wordList):
        wordList.remove(word)
    else:
        return "Not found"
    return wordList

wordList=["Kabil","Dhanush","Pizza","apple"]
word="apple  "
print(removeWord(wordList,word))
