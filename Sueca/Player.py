class Player:

    def __init__(self,name):
        self.name = name
        self.hand = []
        self.score = 0
        self.wcards = []

    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)

    def play_card (self, lead_suit):
       print(f"{self.name}'s turn to play.")
       print(f"Cards in hand: {', '.join(str(c) for c in self.hand)}")
       possible_cards = [c for c in self.hand if c.suit == lead_suit]
       if not possible_cards:
            possible_cards = self.hand
            chosen_card = None
            while not chosen_card:
                try:
                    choice = int(input(f"Choose a card to play (1-{len(possible_cards)})")):
                    chosen_card = possible_cards[choice -1]
                    self.hand.remove(chosen_card)
                except (ValueError, IndexError):
                    print("Invalid choice, please try again.")
            print(f"{self.name} played {chosen_card}.")
            return chosen_card
    
    def add_points(self,points):
        self.score += points
    
    def won_cards(self,card):
        self.wcards.append(card)