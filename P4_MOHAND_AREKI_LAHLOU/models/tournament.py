import random
from datetime import datetime

SELECTION_TIME_CONTROL = ["Bullet", "Blitz", "Rapid"]


class Tournament:
    
    def __init__(self, name, location, description, start_date, end_date, 
                 time_control, players: list[int] = [],
                 rounds: list[Round] = [],
                 actual_round: int=1, number_of_rounds=4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_round = number_of_rounds
        self.actual_round = actual_round
        self.players = players
        self.time_control = time_control
        self.description = description
        self.set_rounds()

    def set_rounds(self)
        for i=1 to self.number_of_round:
            self.round.append(Round(i))
    
    def __str__(self):
        return f"{self.name"