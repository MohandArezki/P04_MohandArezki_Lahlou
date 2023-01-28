# -*- coding: utf-8 -*-

from datetime import datetime
from models.round import Round

SELECTION_TIME_CONTROL = ["Bullet", "Blitz", "Rapid"]
OPEN = True
CLOSE = False


class Tournament:

    def __init__(self, name: str,
                 location: str,
                 description: str,
                 start_date: datetime = datetime.now,
                 end_date: datetime = datetime.now,
                 time_control: int = 0,
                 players: list[int] = [],
                 rounds: list[Round] = [],
                 actual_round: int = 1,
                 number_of_rounds: int = 4,
                 state: bool = OPEN):
        self.id = None         
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_round = number_of_rounds
        self.actual_round = actual_round
        self.players = players
        self.time_control = time_control
        self.description = description
        self.rounds = [Round]*self.number_of_round
        self.state = state

    def setId(self, id):
        self.id = id

    def addPlayer(self, playerId):
        self.players.append(playerId)

    def __str__(self):
        return f"| {self.name :<20} | {self.location :<20} \
                 | {self.start_date} | {self.end_date} \
                 | {self.description :<10} |"
