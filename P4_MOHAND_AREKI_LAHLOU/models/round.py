from random import random
from models.player import Player
from datetime import datetime


class Game:
    """
        class pour gerer les matchs
    """
    def __init__(self, players: [Player]*2 ):

        self.players = players
        self.colors = self.setColors()

    def setColors(self):
        colorOne = random.choice(["Black","White"])
        if colorOne == "Black":
            colorTwo = "White"
        else:
            colorTwo = "Black"
        self.colors = [colorOne, colorTwo]

    def __str__(self):
        return f"{self.id}"


class Round:
    def __init__(self, round: int, games: [Game]):
        self.name = 'Round '+f'{round:02d}'
        self.games = games

    def begin_round(self, date_begin=datetime.now()):
        self.date_begin = date_begin
    
    def end_round(self, date_end=datetime.now()):
        self.date_end = date_end

    def add(self, game: Game):
        """ Add a game in round """
        self.games.append(game)

    def __str__(self):
        """ Return a formatted result"""
        return f"{self.name}"