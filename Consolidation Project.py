# Consolidation Project
# import the modules I will need
import os
import random
# Create a deck of 48 cards, no kings

# List of suits and ranks
suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen']

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f"{rank} of {suit}")


# Shuffle the deck
random.shuffle(deck)

# 8 cards from shuffled desks given to players
player1_deck = deck[:8]
player2_deck = deck[8:16]

print(f"\nPlayer 1's Hand: {len(player1_deck)} cards")
print(f"\nPlayer 2's Hand: {len(player2_deck)} cards")

# Get the scores ready
score_player1 = 0
score_player2 = 0
# Every round one of the cards in the deck is randomly chosen to be shown.
leading_player = random.choice(["Player 1", "Player 2"])
print(f"\n{leading_player} will lead this game.")

# Higher card values will win the round
def card_value(card):
    rank = card.split(' ')[0]
    # Give all the cards certain values
    values = {'Ace': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'Jack': 11, 'Queen': 12}
    return values[rank]

for round_num in range(1, 17):
    print(f"\nROUND {round_num} HAS BEGUN!")
    print(f"Player 1's score: {score_player1}")
    print(f"Player 2's score: {score_player2}")

    print("\nPlayer 1's hand:", player1_deck)
    print("\nPlayer 2's hand:", player2_deck)


    if leading_player == "Player 1":
        print("\nPlayer 1, you are currently the leading player")
        while True:
            card1 = input("Please type a card you would like to play in the format shown above: ")
            if card1 in player1_deck:
                player1_deck.remove(card1)
                break
            else:
                print("This card is not in your hand. please try again.")
    
        print("\nPlayer 2, it is your turn.")
        while True:
            card2 = input("Please type a card you would like to play in the format shown above: ")
            if card2 in player2_deck:
                player2_deck.remove(card2)
                break
            else:
                print("This card is not in your hand. please try again.")
    else: 
    # In a scenario where Player 2 is leading
        print("\nPlayer 2, you are currently the leading player")
        while True:
            card2 = input("Please type a card you would like to play in the format shown above: ")
            if card2 in player2_deck:
                player2_deck.remove(card2)
                break
            else:
                print("This card is not in your hand. please try again.")

        print("\nPlayer 1, it's your turn")
        while True:
            card1 = input("Please type a card you would like to play in the format shown above: ")
            if card1 in player1_deck:
                player1_deck.remove(card1)
                break
            else:
                print("This card is not in your hand. please try again.")

    print(f"\nPlayer 1 has played: {card1}")
    print(f"\nPlayer 2 has played: {card2}")

# Now compare the cards to decide who gets the point
    if card_value(card1) > card_value(card2):
        score_player1 += 1
        leading_player = "Player 1"
        print("Player 1 won this round!!")
    else:
        score_player2 += 1
        leading_player = "Player 2"
        print("Player 2 wins the round!!")

    if deck:
        removed_card = deck.pop(0)
        print(f"A card has been removed from the deck and shown to both players: {removed_card}")
        
    # If both players have 4 cards left, they are dealt 4 cards each.
    if len(player1_deck) == 4 and len(player2_deck) == 4 and len(deck) >= 8:
        print("\nBoth players have 4 cards left. 4 new cards will be dealth to each player.")
        for _ in range(4):
            player1_deck.append(deck.pop(0))
            player2_deck.append(deck.pop(0))

# Ending the game
    # If one players reached 9 points while the other player has at least 1, the game will end as the winner is set.
    if score_player1 == 9 and score_player2 >= 1:
        print("\nPlayer 1 has won the game!")
        break
    elif score_player2 == 9 and score_player1 >= 1:
        print("\nPlayer 2 has won the game!")
        break
    elif score_player1 == 0 and score_player2 == 16:
        print("\nPlayer 1 has shot the moon! Player 1 wins with 17 points!")
        break
    elif score_player2 == 0 and score_player1 == 16:
        print("\nPlayer 2 has shot the moon! Player 2 wins with 17 points!")
        break

print("\nTHE GAME IS NOW OVER")
print(f"Final Scores --- Player 1: {score_player1}, Player 2: {score_player2}")
if score_player1 > score_player2:
    print("Player 1 has won the game!")
elif score_player2 > score_player1:
    print("Player 2 has won the game!")
else:
    print("The game has ended in a tie!")

