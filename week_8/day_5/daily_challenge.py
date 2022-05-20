
import random


class Card:

    def __init__(self):
        self.cards = []
        self.suit = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        self.value = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        for i in range(len(self.value) ):
            for j in range(len(self.suit)):
                self.cards.append((self.value[i], self.suit[j]))


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle_card(self):
        random.shuffle(self.cards)
        return self.cards

    def deal(self, cards_shuffled):

        del cards_shuffled[0]
        return cards_shuffled



my_cards = Card()
print(my_cards.cards)

my_deck = Deck(my_cards.cards)

s = my_deck.shuffle_card()

for i in range(40):
    print(my_deck.deal(s))
