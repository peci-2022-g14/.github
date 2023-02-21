from Deck import Deck
from Team import Team
from Player import Player
import random

class Sueca:
    def __init__(self):
        self.deck = Deck();
        self.deck.shuffle();
        self.teams = [Team(), Team()]
        self.players = []
        self.trump = None
        self.start_player = None
        self.current_player = None
        self.previous_card = None
        self.table = []
        

        #Player sign in and atribuition to a team
        for i in range(4):
            name = input(f"Enter player {i+1}'s name: ")
            player = Player(name)
            self.players.append(player)
            self.teams[i%2].add_player(player)
    
    #Determines the starting player by picking 4 random cards of the Hearts suit, the player with the card with highest value gets to choose the trump card
    #def determine_starting_player(self):
        #self.start_cards = []
        #for player in self.players:
            #card = self.deck.draw()
            #while card.suit != "Hearts":
                #card = self.deck.draw()
            #self.start_cards.append(card)
            #player.add_card(card)
        #self.start_player = self.players[self.start_cards.index(max(self.start_cards, key=lambda x: x.rank))]

        #Returns the cards to the deck and returns the starting player
        #for card in self.start_cards:
            #self.deck.add_card(card)
        #return self.start_player

   #Determines starting player
    def determine_starting_player(self):
            list= []
            list = self.players[:]
            list = random.shuffle(self.list)
            self.start_player = list[0]
    
    #Cut deck function
    def cut_deck(self,deck):
        print(f"The player who cuts is {self.players[(self.start_player.index+2)%len(self.players)].name}")
        cut_index = input(f"Enter cut_index:")
        return deck[cut_index:] + deck[:cut_index]


    #The player chooses the trump card
    def choose_trump(self):
        choice = input("Do you want to draw from the top (T) or bottom (B) of the deck?")
        if choice == "T":
            drawn_card = self.deck.deck.pop(0)
            self.trump = drawn_card.suit
        elif choice == "B":
            drawn_card = self.deck.deck.pop(-1)
            self.trump = drawn_card.suit
        else:
            print("Invalid choice, please try again.")
            self.choose_trump()
        self.start_player[0].add_card(drawn_card)
        print(f"The trump suit is {self.trump}")

        return choice
    
    #Card distribuition, each player gets 10 cards
    """def distribute_cards(self):
        start_player_index = self.players.index(self.start_player)
        for i in range(start_player_index + 4):
            for j in range(9 if i == start_player_index else 10):
                card = self.chec.draw()
                self.players[i % 4].add_card(card)
        for player in self.players:
            print(f"Player {self.players.index(player) + 1}'s hand: {player.hand}")
    """

    def distribute_cards(self, first_player_index,choice):
        if choice == "T":
            first_player = self.players[first_player_index]
            first_player.hand.append(self.deck.pop(0))
            first_player.hand += self.deck[:9]
            self.deck -self.deck[9:]

            for i in range(1, len(self.players)):
                player_index = (first_player_index + i) %len (self.players)
                self.players[player_index].hand = self.deck[:10]
                self.deck - self.deck[10:]
        
        else:
            first_player-self.players[first_player_index]
            first_player.hand.append(self.deck.pop(-1))

            for i in range(1, len(self.players)):
                player_index = (first_player_index + i) %len (self.players)
                self.players[player_index].hand = self.deck[-10:]
                self.deck - self.deck[:-10]
            
            self.players[first_player_index].hand += self.deck

        for player in self.players:
            print(f"Player {self.players.index(player) + 1}'s hand: {player.hand}")
        
            
    #Method to know who is the next player
    def next_player_right(self):
        current_index = self.players.index(self.current_player)
        next_index = (current_index +1) % len(self.players)
        return next_index
    
    def round(self):
        round_cards ={}
        played_cards = []
        current_player = self.start_player
        first_suit = None
        
        
        #first player
        current_card = self.current_player.play_card(first_suit)
        first_suit = current_card.suit
        played_cards.append(current_card)
        round_cards[current_player.name] = current_card
        current_player = self.next_player()
        print(f"{current_player.name} played {current_card}")

        #others
        while len(played_cards) < len(self.players):
            current_card = self.current_player.play_card(first_suit)
            round_cards[current_player.name] = current_card
            played_cards.append(current_card)
            self.next_player()
        
        trump_cards = [card for card in played_cards if card.suit == self.trump]

        if trump_cards:
            winning_card = max(trump_cards, key=lambda card: card.svalue)
            first_suit_cards = [card for card in self.played_cards if card.suit == first_suit]
            winning_card = max(first_suit_cards, key=lambda card: card.svalue)
        
        winning_player = round_cards[winning_card]
        print("Winning player: ", winning_player.name)
        print("Winning card: ", winning_card)

        


    


       

        