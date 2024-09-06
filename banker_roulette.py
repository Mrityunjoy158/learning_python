"""
    Using list and random module.

    First input list of name from user. find the input length.
    Generate randon number 0 and the last index.
    Pick out random person from list of names using the random choice.
"""

import random

name_list = list(map(str, input("Enter Name: ").split()))

name_len = len(name_list)

random_choice = random.randint(0, name_len - 1)

person_who_will_pay = name_list[random_choice]

print(person_who_will_pay + " is going to buy the meal today.")

