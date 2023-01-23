from datetime import datetime

class Game:
    """
        class pour gerer les matchs
    """
    id: int = 0 
    
    def __init__(self, players:{"Player One':{PlayerOne, PlayerTwo],
                 score:[scoreOne,scoreTwo]):
        self.players = players
        self.score = score        

    def __str__(self):
        return f"{self.id}"

class Round:
    """
        class pour gerer les tours.
    """
    def __init__(self, round:int, games: list[Game] = [],
                 date_end=datetime.now()):
        self.name = 'Round '+f'{round:02d}'
        self.games = games
    
    def begin_round(date_begin=datetime.now()):
        self.date_begin = date_begin
    
    def end_round(date_end=datetime.now()):
        self.date_end = date_end

    def add(self, game):
        """ Add a game in round """
        self.games.append(game)

    def __str__(self):
        """ Return a formatted result"""
        return f"{self.name}"