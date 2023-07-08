from hand import Hand

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def add_card(self, card):
        self.hand.add_to_hand(card)

    def get_str_hand(self):
        return str(self.hand)

    def hit(self, deck):
        while self.hand.get_value() < 17:
            self.add_card(deck.deal())
