# -*- coding: utf-8 -*-
import datetime

SELECTION_GENDER = ["Homme", "Femme", "Autre"]


class Player:

    def __init__(self, ine: str, firstname: str, lastname: str, date_of_birth: datetime,
                 gender: int, rank:int=0, score:int=0):
        """
        create a player 
        """                 
        self.ine = ine
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.gender = SELECTION_GENDER[gender]
        self.rank = rank
        self.score = score
 
    def setRank(self, rank):
        self.rank = rank
    
    def setScore(self, score):
        self.score = score

    def __str__(self):
        return f"{self.ine}"

   