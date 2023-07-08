import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        return [Card(s, v) for s in range(4) for v in range(13)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
