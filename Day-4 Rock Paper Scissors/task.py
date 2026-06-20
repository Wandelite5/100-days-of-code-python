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
import random
my_list = [rock, paper, scissors]
names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}

user = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors"))
computer = random.choice(my_list)
print(f"Computer chose:{names[computer]}\n {computer}")

if user == 0: #rock
    if computer == scissors:
        print("You Win")
    elif computer == paper:
        print("You Lose")
    else:
        print("It is a tie")
elif user == 1: # paper
    if computer == scissors:
        print("You lose")
    elif computer == rock:
        print("You Win")
    else:
        print("It is a tie")
elif user == 2: #scissors
    if computer == rock:
        print("You lose")
    elif computer == paper:
        print("You Win")
    else:
        print("It is a tie")
else:
    print("Enter a valid number")