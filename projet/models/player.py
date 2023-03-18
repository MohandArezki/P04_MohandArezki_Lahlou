# -*- coding: utf-8 -*-


class Player:
    def __init__(self,
                 name,
                 firstname,
                 date_of_birth,
                 gender,
                 rank=0,
                 id=None):
        self.id = id
        self.lastname = name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rank = rank

    @property
    def fullname(self) -> str:
        return f"{self.lastname}, {self.firstname}"
