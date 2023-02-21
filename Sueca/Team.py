class Team:

    def __init__(self,players):
        self.players = players
        self.score = 0
    
    def add_points (self,points):
        self.score += points

    def add_player (self,player):
        self.player = player
