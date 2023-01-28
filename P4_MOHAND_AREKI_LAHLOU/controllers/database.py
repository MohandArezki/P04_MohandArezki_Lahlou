# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query
from models.player import Player
from models.tournament import Tournament


class Database:
    """
    the database directory and file name : /data/chess_db.json
    there is tables :
    table 1 : players
    table 2 : tournaments
    """
    # class variables
    db = TinyDB('data/chess_db.json')
    tb_players = db.table('Players')
    tb_tournaments = db.table('Tournaments')
    tb_rounds = db.table('Rounds')
    tb_games = db.table('Games')
    playersList = []
    tournamentsList = []

    def load():
        players_dict = Database.tb_players.all()
        for player_dict in players_dict:
            player = Player(
                player_dict["INE"],
                player_dict["Firstname"],
                player_dict["Lastname"],
                player_dict["Date Of Birth"],
                player_dict["Gender"],
                player_dict["Rank"],
                player_dict["Score"])
            player.setId(player_dict.doc_id)
            Database.playersList.append(player)
        tournaments_dict = Database.tb_tournaments.all()
        for tournament_dict in tournaments_dict:
            tournament = Tournament(
                tournament_dict["Name"],
                tournament_dict["Location"],
                tournament_dict["From"],
                tournament_dict["To"])
               # tournament_dict["Number of Rounds"],
               # tournament_dict["Actual Round"],
              #  tournament_dict["Players"],
              #  tournament_dict["Time Control"],
              #  tournament_dict["Description"],
              #  tournament_dict["Rounds"])
            tournament.setId(tournament_dict.doc_id)
            Database.tournamentsList.append(tournament)

    def insert_player(player: Player):
        """Add player object in database."""
        document = Database.playerAsDocument(player)
        player_query = Query()
        if Database.tb_players.search(player_query.INE == document.get("INE")):
            print("Code INE déjà saisi !")
        else:
            Database.tb_players.insert(document)
            print("Joueur Sauvegardé !")
            # Set the id of the new saved player 
            player.setId(Database.tb_players.all()[-1].doc_id)

    def update_player(player: Player):
        """ Update player object in database."""
        document = player.getDocument()
        player_query = Query()
        if Database.tb_players.search(player_query.INE == document.get("INE")):
            print("Code INE déjà saisi !")
        else:
            Database.tb_players.Update(document)
            print("Joueur Sauvegardé !")
            # Set the id of the new saved player
            player.setId(Database.tb_players.all()[-1].doc_id)

    def insert_tournament(tournament: Tournament):
        """Add tournament object in database."""
        document = Database.tournamentAsDocument()
        tournament_query = Query()
        if not Database.tb_tournament.search(tournament_query.name == document.get("Name")):
            print("Tournoi déjà saisi !")
        else:
            Database.tb_tournament.insert(document)
            print("Tournoi Sauvegardé !")
            # Set the id of the new saved tournament
            tournament.id = Database.tb_tournament.all()[-1].doc_id

    def tournamentAsDocument(self, tournament: Tournament):
        document = {"Name": tournament.name,
                    "Location": tournament.location,
                    "From": tournament.start_date,
                    "To": tournament.end_date,
                    "Number of Rounds": tournament.number_of_rounds,
                    "Actual Round": tournament.actual_round,
                    "Players": tournament.players,
                    "Time Control": tournament.time_control,
                    "Description": tournament.description,
                    "Rounds": tournament.rounds}
        return document

    def playerAsDocument(self, player: Player):
        document = {"INE": player.model.ine,
                    "Firstname": player.model.firstname,
                    "Lastname": player.model.lastname,
                    "Date Of Birth": player.model.date_of_birth,
                    "Gender": player.model.gender,
                    "Rank": player.model.rank,
                    "Score": player.model.score}
        return document

    def save_tournament():
        pass

    def save_roud():
        pass

    def save_game():
        pass
