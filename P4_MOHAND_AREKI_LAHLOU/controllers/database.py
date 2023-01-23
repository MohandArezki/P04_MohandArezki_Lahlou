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
    DB =  TinyDB('data/chess_db.json')
    TB_PLAYERS = db.table('Players')
    TB_TOURNAMENTS = db.table('Tournaments')
    TB_ROUNDS = db.table('Rounds')
    TB_GAMES = db.table('Games')
    
    players =[]
    
    def insert_player_in_db():
        """Add player object in database."""
        serialized_player = {"INE":"AB12388","Firstname":"Daniel","Lastname":"Bernier","Date Of Birth":"20/11/1995","Gender":1,"Rank":25,"Score":17}
        """
         serialized_player = {'INE':self.ine,
                             'Firstname':self.firstname,
                             'Lastname':self.lastname,
                             'Date Of Birth':self.date_of_birth,
                             'Gendre':self.gender
                             'Rank':self.rank,
                             'Score'self.score = score}
        """                             
        User = Query()
        if not Database.tb_test.search(User.INE ==serialized_player.get("INE") ):
            print("Code INE déjà saisi !")        
        else 
            Database.tb_players.insert(serialized_player)
            print("Joueur Sauvegardé !")


    def insert_tournament_in_db():
        """Add player object in database."""
         serialized_tournament = {'Name': "International Chess Tournament"
        "Location":"Paris, France",
        "From":"10/01/2023",
        "To":"25/01/2023",
        "Number of Rounds":4,
        "Actual Round": 1
        "Players":[1,2,5,7,8,10,11,14,13],
        "Time Control":1,
        "Description":" Descritpuion of international Chess Tournament",
        "Rounds":[15,16,17,18]}
        
        
        tournament = Query()
        if not Database.tb_tournament.search(tournament.name ==serialized_tournament.get("Name") ):
            print("Tournoi déjà saisi !")
        else   
            Database.tb_tournament.insert(serialized_tournament)


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
        db.remove(where('key') == 1)

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

    