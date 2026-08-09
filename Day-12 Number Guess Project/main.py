import random
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)

user_guess = input("Choose a difficulty. Type 'easy' or 'hard': ")

game_over = False
if user_guess == 'easy':
    attempts = 10
else:
    attempts = 5

def check_guess(guess, answer):
    # compare guess to answer
    if guess == answer:
    # correct: print win message, return True
        print(f"Congratulations! You guessed the number {answer}.")
        return True
    # too low or too high: print which, return False
    elif guess < answer:
        print(f"Sorry, you guessed a low number {guess}.")
        return False
    else:
        print(f"Sorry, you guessed a high number {guess}.")
        return False
    # no loop in here, don't touch attempts in here

while not game_over and attempts > 0:
    # ask the player for a number
    user_guess = int(input("Choose a number: "))
    # call check_guess(...) and look at what it hands back
    correct = check_guess(user_guess, answer)
    # if True: game_over = True
    if correct:
        game_over = True
    else:
        attempts -= 1
        print(f"Attempts left {attempts}.")
    # if False: attempts -= 1   (this line lives in the loop)


# after the loop:
# if they never got it, reveal the number


if attempts == 0:
    print(f'The number I was thinking of was {answer}')







