# -*- coding: utf-8 -*-
from repositories.database import Database
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from repositories.player import PlayerRepository


class TournamentRepository:
    def __init__(self):
        """
        Initializes a new instance of the TournamentRepository class.
        """
        self.players_repository = PlayerRepository()
        self.table = Database.tournament_table

    def get_all_tournaments(self):
        """
        Returns a list of all tournaments from the database.

        Returns:
            A list of Tournament objects.
        """
        tournaments = []
        for doc in self.table.all():
            tournaments.append(self.deserialize({**{"ID": doc.doc_id}, **doc}))
        return tournaments

    def get_tournament(self, id):
        """
        Returns a tournament with the specified ID from the database.

        Args:
            id (int): The ID of the tournament to retrieve.

        Returns:
            A Tournament object if found, None otherwise.
        """
        doc = self.table.get(doc_id=id)
        if doc:
            return self.deserialize({**{"ID": id}, **doc})

        return None

    def add_tournament(self, tournament):
        """
        Adds a tournament to the database.

        Args:
            tournament (Tournament): The Tournament object to add.
        """

        self.table.insert(self.serialize(tournament))

    def update_tournament(self, tournament):
        """
        Updates a tournament in the database.

        Args:
            tournament (Tournament): The Tournament object to update.
        """
        self.table.update(self.serialize(tournament), doc_ids=[tournament.id])

    def delete_tournament(self, id):
        """
        Deletes a tournament from the database.

        Args:
            id (int): The ID of the tournament to delete.
        """
        self.table.remove(doc_ids=[id])

    def serialize(self, tournament) -> dict:
        """
        Serialize a Tournament object to a dictionary.

        Args:
            tournament (Tournament): The Tournament object to be serialized.

        Returns:
            dict: A dictionary containing the serialized tournament data.
        """
        players = []
        rounds = []
        players = [player.id for player in tournament.players]
        for round in tournament.rounds:
            matchs = []
            for match in round.matchs:
                opponents = {"White": match.players["White"].id,
                             "Black": match.players["Black"].id}
                result = {"White": match.scores["White"],
                          "Black": match.scores["Black"]}
                matchs.append({"Players": opponents, "Scores": result})
            rounds.append({"Round": round.round_number,
                           "Status": round.state,
                           "Begin Date": round.begin_date,
                           "End Date": round.end_date,
                           "Matchs": matchs
                           })
        return {
            "Tournament": tournament.name,
            "Location": tournament.location,
            "Time control": tournament.time_control,
            "Description": tournament.description,
            "Number of players": tournament.number_of_players,
            "Number of rounds": tournament.number_of_rounds,
            "Status": tournament.state,
            "Begin date": tournament.begin_date,
            "End Date": tournament.end_date,
            "Players": players,
            "Rounds":  rounds
        }

    def deserialize(self, json_dict: dict) -> 'Tournament':
        """
        Deserialize a Tournament object from a dictionary.

        Args:
            json_dict (dict): A dictionary containing the serialized tournament data.

        Returns:
            Tournament: A Tournament object.
        """
        players_dict = json_dict["Players"]
        players_obj = []
        for player_id in players_dict:
            player = self.players_repository.get_player(player_id)
            players_obj.append(player)

        rounds_obj = []
        for round_dict in json_dict["Rounds"]:
            matchs_dict = []
            for match_dict in round_dict["Matchs"]:
                player_w = self.players_repository.get_player(match_dict["Players"]["White"])
                player_b = self.players_repository.get_player(match_dict["Players"]["Black"])
                score_w = match_dict["Scores"]["White"]
                score_b = match_dict["Scores"]["Black"]
                match = Match(player_w, player_b)
                match.set_result(score_w, score_b)
                matchs_dict.append(match)
            round_obj = Round(round_dict["Round"])
            round_obj.matchs = matchs_dict
            round_obj.state = round_dict["Status"]
            round_obj.begin_date = round_dict["Begin Date"]
            round_obj.end_date = round_dict["End Date"]
            rounds_obj.append(round_obj)

        return Tournament(
            name=json_dict["Tournament"],
            location=json_dict["Location"],
            time_control=json_dict["Time control"],
            description=json_dict["Description"],
            number_of_players=json_dict["Number of players"],
            number_of_rounds=json_dict["Number of rounds"],
            state=json_dict["Status"],
            begin_date=json_dict["Begin date"],
            end_date=json_dict["End Date"],
            players=players_obj,
            rounds=rounds_obj,
            id=json_dict['ID']
        )
