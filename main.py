from art import *
from game_data import data
import random
from clearScreen import cls

def higherLower():
    continues = True
    score = 0
    print (logo)
    quesA = random.choice(data)
    quesB = random.choice(data)
    while continues:        
        print (f"Compare A: {quesA['name']}, {quesA['description']} from {quesA['country']}")
        print (vs)
        print (f"Against B: {quesB['name']}, {quesB['description']} from {quesB['country']}")
        qqq = input("Who has more followers? A or B?    ").lower()
        if quesA['follower_count'] > quesB['follower_count']:
            if qqq == "a":
                cls()
                score += 1
                print ("Correct!")
                print (f"Current score is {score}")
                quesA == quesA
                quesB = random.choice(data)
            elif qqq == "b":
                cls()
                print ("Incorrect, game over.")
                print (f"Final score: {score}")
                continues = False
        else:
            if qqq == "b":
                cls()
                score += 1
                print ("Correct!")
                print (f"Current score is {score}")
                quesA = quesB
                quesB = random.choice(data)
            elif qqq == "a":
                cls()
                print ("Incorrect, game over.")
                print (f"Final score: {score}")
                continues = False




higherLower()