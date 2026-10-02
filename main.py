#main.py runs everything

from scoring import score_number, score_three_of_a_kind, score_four_of_a_kind, score_five_of_a_kind, score_3OfAKind_and_2OfAKind, score_chance

import random

#rolling for both user
def roll_dice(dice,held):
    for i in range(5): #5dice
        if not held[i]:
            dice[i] = random.randint(1,6)
    return dice

def hold_dice(held, index):
    held[index] = not held[index]


for round in range(2):
    print(f"===========ROUND {round+1} ==============")
    red_dice = ['*'] * 5 #initial placeholder
    blue_dice = ['*'] * 5

    red_held = [False] * 5
    blue_held = [False] * 5

    #for red(user) turns
    print("--------RED(USER) TURN--------")
    for i in range(3): #0-2 3rolls
        print(roll_dice(red_dice,red_held))

        if i!=2 : #except roll3 
            n = int(input("How many dice do you want to hold?"))

            for j in range(n):
                num = int(input("Enter which die do you want to hold(1-5)?"))
                if num > 0 and num <= 5: #5ota dice ko range
                    hold_dice(red_held,num-1) #0-4 lai 1-5

    #for blue(bot) turns
    print("--------BLUE(BOT) TURN--------")
    for i in range(3): #0-2 3rolls
        print(roll_dice(blue_dice,blue_held))

        if i!=2 : #except roll3
            for j in range(5): #5ota dice ko range (0-4)-5
                if blue_dice[j]==6 or blue_dice[j]==5:
                    hold_dice(blue_held,j) 

