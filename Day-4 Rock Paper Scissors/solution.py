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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
''''
The whole thing rests on the order you assigned: 0 = rock, 1 = paper, 2 = scissors. 
That order isn't random — it follows the real game. Each item beats the one before it:
paper (1) beats rock (0)
scissors (2) beats paper (1)
Whoever has the higher number wins. If the computer's number is bigger, you lose. 
If yours is bigger, you win. That single rule correctly handles paper-vs-rock and scissors-vs-paper, because in both
of those the higher number really does win. **But the rule has one exception. There's a "wrap-around" in 
rock-paper-scissors: the lowest beats the highest. Rock (0) beats scissors (2). Here the lower number wins, 
which breaks the "higher wins" rule. So that one case has to be caught before the general rule runs:
'''
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice]) 

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
