#yahtzee scorings players

def score_number(dice,number):
    #1-6 sums
    return number * dice.count(number) 

def score_three_of_a_kind(dice):
    for number in range(1,7):
        if dice.count(number)>=3:
            return sum(dice)
    return 0

def score_four_of_a_kind(dice):
    for number in range(1,7):
            if dice.count(number)>=4:
                return sum(dice)
    return 0

def score_five_of_a_kind(dice):
    for number in range(1,7):
            if dice.count(number)>=5:
                return 50
    return 0

def score_3OfAKind_and_2OfAKind(dice):
    counts = [dice.count(number) for number in set(dice)]
    if 3 in counts and 2 in counts:
        return 25
    return 0

def score_chance(dice):
    return sum(dice)