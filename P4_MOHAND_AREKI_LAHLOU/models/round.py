from datetime import datetime

class Game:
    """
        class pour gerer les matchs
    """
    id: int = 0 
    
    def __init__(self, players:{"Player One':{PlayerOne, PlayerTwo],
                 score:[scoreOne,scoreTwo]):
        self.id = self.getID()       
        self.players = players
        self.score = score        

    def getID(self):
        Game.id =Game.id + 1  
        return Game.id

    def __str__(self):
        return f"{self.id}"


class Round:
    """
        class pour gerer les tours.
    """
    id:int = 0 
    
    def __init__(self, name, games: list[Game] = [],
                 date_end=datetime.now()):
        self.id = self.getID()         
        self.name = name
        self.date_begin = date_begin
        self.date_end = date_end
        self.games = games
    
    def getID(self):
        Round.id =Round.id + 1  
        return Round.id

    
    def begin_round(date_begin=datetime.now()):
        self.date_begin = date_begin
    
    def end_round(date_end=datetime.now()):
        self.date_end = date_end

    def add(self, game):
        """ Add a game in round """
        self.games.append(game)

    def __str__(self):
        """ Return a formatted result"""
        return f"{self.id}"