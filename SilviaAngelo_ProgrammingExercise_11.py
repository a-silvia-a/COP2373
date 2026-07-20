#Using the Deck object, game program will deal a Poker hand of five cards.
#Then prompt the user to enter a series of numbers (for example: 1, 3, 5)
#that selects cards to be replaced during a draw phrase.
#Then print the result of drawing the new cards.

import random

class Deck:
    def __init__(self, size=52):
        #Initializes the deck of cards.
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discard_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discard_list)
            self.card_list = self.discard_list
            self.discard_list = []
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        #Clears active cards back into the discard pile.
        self.discard_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

#Lists of all possible cards, loops through the 5 cards and numbers them
def print_hand(hand):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for index, card in enumerate(hand, start=1):
            r = card % 13
            s = card // 13
            #Prints cards in order form.
            print(f"{index}: {ranks [r]} of {suits[s]}")

#Groups cards into mutable list.
def deal_hand(deck, hand_size=5):
    hand = []
    for i in range (hand_size):
        hand.append(deck.deal())
    return hand

#Takes number of cards that user wants to replace.
def replace_cards(hand, deck, choices_string):
        choices = choices_string.split(",")
        for choice in choices:
            index = int(choice) - 1
            hand[index] = deck.deal()
        return hand

#Main function to executes dealing of hands
def main():
    #Initialize and shuffle
    game_deck = Deck()

    print("Your Starting Hand")
    #Populate the player's initial list container
    my_hand = deal_hand(game_deck)
    print_hand(my_hand)

    discard_input = input("\nEnter card numbers to replace (e.g. 1,3,5) or press Enter to stay:")

    #Executes draw replacements or keep original choices
    if discard_input.strip():
        my_hand = replace_cards(my_hand, game_deck, discard_input)
        print("\n Your Final Hand After Draw")
        print_hand(my_hand)
    else:
        print("\n Keeping your original hand.")

if __name__ == "__main__":
    main()


