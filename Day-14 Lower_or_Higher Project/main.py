import random
import art
from game_data import data

import art
from game_data import data
import random
def play_game():
    chosen_A = random.choice(data)
    chosen_B = random.choice(data)
    game_over = False
    current_score = 0

    while not game_over:
        print(art.logo)
        print(f"Compare A: {chosen_A['name']}, a {chosen_A['description']}, from {chosen_A['country']}")
        print(art.vs)
        print(f"Against B:  {chosen_B['name']}, a {chosen_B['description']}, from {chosen_B['country']}")
        compare = input("Who has more followers? Type 'A' or 'B':").strip().upper()
        A = chosen_A['follower_count']
        B = chosen_B['follower_count']
        if A == B:
            chosen_A = chosen_B
            chosen_B = random.choice(data)
        elif compare == 'A' and A > B:
            current_score += 1
            chosen_B = random.choice(data)
        elif compare == 'A' and A < B:
            game_over = True
            print(f"You lose! The final score is {current_score}")
        elif compare == 'B' and B > A:
            current_score += 1
            chosen_A = chosen_B
            chosen_B = random.choice(data)
        else:
            game_over = True
            print(f"You lose! The final score is {current_score}")

# After the play loss ask do you want to play again?
    play_again = input("Do you want to play again? Type 'Y' or 'N':").strip().upper()
    if play_again == 'Y':
        play_game()
    else:
        exit()
play_game()
