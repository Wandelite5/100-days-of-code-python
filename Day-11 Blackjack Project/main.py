import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# deal_card(): return a random card from the list
def deal_card():
    return random.choice(cards)


# calculate_score(card_list):
def calculate_score(card_list):
    #   - return 0 if it's a Blackjack (2 cards summing to 21)
    if len(card_list) == 2 and 11 in card_list and sum(card_list) == 21:
        return 0
    #   - if score > 21 and hand has an 11 (Ace), convert 11 to 1
    while 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    #   - return the sum
    return sum(card_list)


# compare(user_score, computer_score): return the result message
def compare(user_score, computer_score):
    #   - check busts first, then Blackjacks, then draw, then higher score
    if user_score > 21:
        print("User busts")
    elif computer_score > 21:
        print("Computer busts")
    elif user_score == 0:
        print("User wins")
    elif computer_score == 0:
        print("Computer wins")
    elif user_score == computer_score:
        print("There is a tie")
    elif user_score > computer_score:
        print("User wins")
    else:
        print("Computer wins")


# Initialize empty hands for user and computer, and game_over flag  - lists to store values and Boolean value to start game
user_list = []
computer_list = []
game_over = False

# Deal 2 cards to each — ONCE, before the loop
for _ in range(2):
    user_list.append(deal_card())
    computer_list.append(deal_card())

# USER'S TURN (loop):
while not game_over:
    #   - calculate both scores
    user_score = calculate_score(user_list)
    computer_score = calculate_score(computer_list)
    #   - show user's cards + score, and computer's first card
    print(f"{user_list} + {user_score}")
    print(f"Computer's first card {computer_list[0]}")
    #   - end if user has Blackjack, computer has Blackjack, or user busts
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    #   - otherwise ask to hit or pass; hit = deal one card, pass = end turn
    else:
        get_another_card = input("type 'y' to deal one card or 'n' to end turn")
        if get_another_card == 'y':
            user_list.append(deal_card())
        else:
            game_over = True

# COMPUTER'S TURN:
#   - keep looping while computer's score is below 17 (dealer must keep drawing)
#   - stop early if computer already has 21
#   - each loop: deal one card, then recalculate the score so the while-check is up to date
while computer_score != 0 and computer_score < 17:
    computer_list.append(deal_card())
    computer_score = calculate_score(computer_list)

# FINAL COMPARISON — print both final hands and the result
print(f"Your final hand: {user_list}, score: {user_score}")
print(f"Computer's final hand: {computer_list}, score: {computer_score}")
compare(user_score, computer_score) 