# -*- coding: utf-8 -*-
from repositories.database import Database
from models.player import Player


class PlayerRepository:
    def __init__(self):
        self.table = Database.player_table

    def get_all_players(self):
        """
        Returns a list of all the players in the database.
        """
        players = []
        for doc in self.table.all():
            players.append(self.deserialize({**{"ID": doc.doc_id}, **doc}))
        return players

    def get_player(self, id):
        """
        Returns a player object based on the ID provided.
        Args:
            id (int): The ID of the player to retrieve.

        Returns:
            A Player object if the player exists, None otherwise.
        """
        doc = self.table.get(doc_id=id)
        if doc:
            return self.deserialize({**{"ID": id}, **doc})
        return None

    def add_player(self, player):
        """
        Adds a player to the database.
        Args:
            player (Player): The player object to add to the database.
        """
        self.table.insert(self.serialize(player))

    def update_player(self, player):
        """
        Updates an existing player in the database.
        Args:
            player (Player): The player object to update in the database.
        """
        self.table.update(self.serialize(player), doc_ids=[player.id])

    def delete_player(self, id):
        """
        Deletes a player from the database based on the ID provided.
        Args:
            id (int): The ID of the player to delete.
        """
        self.table.remove(doc_ids=[id])

    def serialize(self, obj) -> dict:
        """
        Returns a dictionary containing the player's data for serialization.
        """
        return {
            "Lastname": obj.lastname,
            "Firstname": obj.firstname,
            "Date of birth": obj.date_of_birth,
            "Gender": obj.gender,
            "Rank": obj.rank
        }

    def deserialize(self, json_dict: dict) -> 'Player':
        """
        Returns a Player object from the provided JSON dictionary.
        Args:
            json_dict (dict): A dictionary containing the player's data for deserialization.

        Returns:
            A Player object.
        """
        return Player(json_dict['Lastname'],
                      json_dict['Firstname'],
                      json_dict['Date of birth'],
                      json_dict['Gender'],
                      json_dict['Rank'],
                      json_dict['ID'])
