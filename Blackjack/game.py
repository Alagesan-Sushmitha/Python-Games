from deck import Deck

class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.deck = Deck()

    def hit_or_stay(self):
        while True:
            decision = input("Do you want to (H)it or (S)tay? ").lower()
            if decision in ['h', 's']:
                return decision
            else:
                print("Invalid input, please enter H for Hit or S for Stay.")

    def start_game(self):
        self.deck.shuffle()
        self.player.add_cards(self.deck.deal(), self.deck.deal())
        self.dealer.add_card(self.deck.deal())

        print(f"Your cards: {self.player.show_cards()}")
        print(f"Dealer's cards: {self.dealer.get_str_hand()}")
        
        while True:
            decision = self.hit_or_stay()
            if decision == 'h':
                self.player.hit(self.deck)
                print(f"Your cards: {self.player.show_cards()}")
                if self.player.hand.get_value() == 21:
                    print("Blackjack! You won.")
                    return
                elif self.player.hand.get_value() > 21:
                    print("Busted! You lost.")
                    return
            else:
                break

        self.dealer.hit(self.deck)
        print(f"Dealer's cards: {self.dealer.get_str_hand()}")
        if self.dealer.hand.get_value() > 21:
            print("Dealer busted! You win!")
        elif self.dealer.hand.get_value() > self.player.hand.get_value():
            print("You lost!")
        elif self.dealer.hand.get_value() < self.player.hand.get_value():
            print("You won!")
        else:
            print("It's a draw!")
