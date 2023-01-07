import random

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

# Write your code below this line 👇

user_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n")

if user_choice == "0":
    print("Rock\n", rock)
elif user_choice == "1":
    print("Paper\n", paper)
elif user_choice == '2':
    print("Scissors\n", scissors)


options = [rock, paper, scissors]
computer_choice = random.choice(options)

print(computer_choice)


if computer_choice == rock:
    print("Rock")
elif computer_choice == paper:
    print("Paper")
elif computer_choice == scissors:
    print("Scissors")


if user_choice == "0" and computer_choice == scissors:
    print("You win")
elif user_choice == "2" and computer_choice == paper:
    print("You win")
elif user_choice == "1" and computer_choice == rock:
    print("You win")
else:
    print("You lose")
