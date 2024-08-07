"""
The game() function in a program lets a user play a game and 
returns the score as an integer. you need to read a file 'Hiscore.txt' 
which is either blank or contains the previous Hi-score. you need to 
write a program to update the Hi-score whenever game() breaks the Hi-score.
"""
import random
def game():
    score=random.randint(1,100)
    print(f'The score is {score}')
    return score

score=game()
with open("Hiscore.txt","r") as f:
    hiscore=int(f.read())
if(hiscore<score):
    with open("Hiscore.txt","w") as f:
        f.write(str(score))
