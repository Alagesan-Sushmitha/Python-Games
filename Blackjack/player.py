from hand import Hand

class Player:
    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()

    def add_cards(self, *cards):
        for card in cards:
            self.hand.add_to_hand(card)

    def show_cards(self):
        return str(self.hand)

    def hit(self, deck):
        self.add_cards(deck.deal())
