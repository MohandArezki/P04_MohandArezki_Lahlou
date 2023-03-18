# -*- coding: utf-8 -*-
import os
from tinydb import TinyDB


class Database:
    """
    A class to handle database interactions using TinyDB.

    Attributes:
    - db (TinyDB): the TinyDB instance used to manage the database file.
    - player_table (Table): a table in the database to store player data.
    - tournament_table (Table): a table in the database to store tournament data.
    """
    db = TinyDB(os.getcwd() + r"/data/db/chess_tournament.json")
    player_table = db.table('Players')
    tournament_table = db.table('Tournaments')
