import random
"""
Rock, peper and scissors game rules.

Rock wins against scissors; 
paper wins against rock; 
scissors wins against paper.
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]
user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Peper, "
                        "2 for Scissors.\n"))

if 0 <= user_choice <= 2:
    print(game_image[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: ")
    print(game_image[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw")
else:
    print("You typed invalid number, you lose")

