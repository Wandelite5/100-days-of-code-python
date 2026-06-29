import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(card_list):
    # Returns 0 for blackjack (2 cards: ace + 10), converts ace from 11 to 1 if bust
    if len(card_list)==2 and 11 in card_list and sum(card_list) == 21:
        return "Blackjack"
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


# 1. Initialize empty hands
user_cards = []
computer_cards = []

# Deal two cards each to start
# The _ is just a throwaway variable — it means I don't care about the loop counter,
# You'll see that pattern a lot in Python.
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
if user_score == 'Blackjack':
    print("You win!")
elif computer_score == 'Blackjack':
    print("Computer wins!")
elif user_score > 21:
    print("You Lose!")
elif computer_score > 21:
    print("Computer wins!")
print(user_cards)
print(user_score)

interested_user = input("Do you want to play a game of Black Jack ? Type 'y' or 'n': ")
