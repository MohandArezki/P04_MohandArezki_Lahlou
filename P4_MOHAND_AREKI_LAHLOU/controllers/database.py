# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query
from models.player import Player

class Database:
    """
    the database directory and file name : /data/chess_db.json
    there is tables :
    table 1 : players
    table 2 : tournaments
    """ 
    # class variables

    DB_FILENAME = 'data/chess_db.json'
    PLAYERS_TB_NAME = 'players'
    TOURNAMENT_TB_NAME = 'tournaments'
    database =  TinyDB(DB_FILENAME)
    tb_players = database.table(PLAYERS_TB_NAME)
    players =[]

    def load_players():
        players_dict = Database.tb_players.all()
        players = []
        for player_dict in players_dict :
            players.append(Player(
                player_dict["INE"],
                player_dict["Firstname"],
                player_dict["Lastname"],
                player_dict["Date Of Birth"],
                player_dict["Gender"],
                player_dict["Rank"],
                player_dict["Score"]))
        return (players)
    
    def remove_player():
        database.remove(where('key') == 1)
        
    
    def serialize_player(self):
        result = {"INE":self.ine,
                  "Firstname":self.firstname,
                  "Lastname":self.lastname,
                  "Date Of Birth":self.date_of_birth,
                  "Gender":self.gender,
                  "Rank":self.rank,
                  "Score":self.score}
        return result                  
 
    def save_player():
        serialize_player()
        pass
    
    def load_tournaments():
        pass

    def save_tournament():
        #serialize_tournament()
        pass
    
    def save_roud():
        #serialize_round()
        pass

    def save_game():
        #serialize_game()
        pass

    