class Hand:
    def __init__(self):
        self.cards = []

    def add_to_hand(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.value >= 10:
                value += 10
            elif card.value == 0:  # Ace
                value += 11
                aces += 1
            else:
                value += card.value + 1
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
