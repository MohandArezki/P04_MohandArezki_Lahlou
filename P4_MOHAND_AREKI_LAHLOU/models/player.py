# -*- coding: utf-8 -*-
import datetime

SELECTION_GENDER = ['Autre', 'Homme', 'Femme']


class Player:
    """
        class to manage a player as objet
        create  player1
           player1 = Player('AB123456','John','Doe','15/10/1990')
        set id to player1
           player1.setId(15)
        change the rank of player1
            player1.rank(18)
        change the score of player1, 
            player1.score(10)
            will add 10 to the player1 's old score
    """
    def __init__(self, ine: str,
                 firstname: str,
                 lastname: str,
                 date_of_birth: datetime,
                 gender: int = 0,
                 rank: int = 0,
                 score: int = 0):
        self.id = None
        self.ine = ine
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.gender = SELECTION_GENDER[gender]
        self.rank = rank
        self.score = score

    def setId(self, id):
        self.id = id

    def setRank(self, rank):
        self.rank = rank

    def setScore(self, score):
        self.score = self.score + score

    def __str__(self):
        return f"| {self.ine :<10} | {self.firstname :<20} | {self.lastname :<20} | \
                 {self.date_of_birth :<10} | {self.gender :<10} | {self.rank :<8} | {self.score :<8} |"
