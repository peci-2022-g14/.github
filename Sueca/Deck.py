class Deck:

    def __init__(self):
        suits = ['hearts','spades', 'diamonds','clubs']
        ranks = ['2','3','4','5','6','7','Queen','Jack','King','Ace']
        self.cards = [(rank, suit, value) for suit in suits for rank, value in zip(ranks, [0,0,0,0,0,10,2,3,4,11])]
        self.cards = [(rank, suit, svalue) for suit in suits for rank, svalue in zip(ranks, [1,2,3,4,5,6,7,8,9,10])]
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

        