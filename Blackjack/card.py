class Card:

    SUIT_SYMBOLS = ["♠", "♥", "♦", "♣"]
    VALUE_NAMES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.VALUE_NAMES[self.value]}{self.SUIT_SYMBOLS[self.suit]}"
