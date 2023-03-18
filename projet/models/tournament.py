# -*- coding: utf-8 -*-
from datetime import datetime
from models.player import Player
from models.round import Round

CREATED = "Created"
IN_PROGRESS = "In Progress"
CLOSED = "Closed"

BULLET = "B"
BLITZ = "Z"
RAPID = "R"


class Tournament:
    """
    Represents a chess tournament.

    Attributes:
        id (int): the unique identifier of the tournament.
        name (str): the name of the tournament.
        location (str): the location of the tournament.
        time_control (int): the time control of the tournament (0 for bullet, 1 for blitz, and 2 for rapid).
        description (str): the description of the tournament.
        number_of_players (int): the number of players in the tournament.
        number_of_rounds (int): the number of rounds in the tournament.
        begin_date (str): the date when the tournament starts.
        end_date (str): the date when the tournament ends.
        state (str): the state of the tournament (either 'Created', 'In Progress', or 'Closed').
        players (list): a list of players in the tournament.
        rounds (list): a list of rounds in the tournament.

    """

    def __init__(self,
                 name="",
                 location="",
                 time_control=BLITZ,
                 description="",
                 number_of_players=0,
                 number_of_rounds=4,
                 begin_date="",
                 end_date="",
                 state=CREATED,
                 players: list[Player] = [],
                 rounds: list[Round] = [],
                 id=None,
                 ):
        """
        Initializes a new instance of the Tournament class.

        Args:
            id (int): the unique identifier of the tournament.
            name (str): the name of the tournament.
            location (str): the location of the tournament.
            time_control (int): the time control of the tournament (0 for bullet, 1 for blitz, and 2 for rapid).
            description (str): the description of the tournament.
            number_of_players (int): the number of players in the tournament.
            number_of_rounds (int): the number of rounds in the tournament.
            begin_date (str): the date when the tournament starts.
            end_date (str): the date when the tournament ends.
            state (str): the state of the tournament (either 'Created', 'In Progress', or 'Closed').
            players (list): a list of players in the tournament.
            rounds (list): a list of rounds in the tournament.
        """
        self.id = id
        self.name = name
        self.location = location
        self.time_control = time_control
        self.description = description
        self.number_of_players = number_of_players
        self.number_of_rounds = number_of_rounds
        self.begin_date = begin_date
        self.end_date = end_date
        self.state = state
        self.players = players
        self.rounds = rounds
        self.init_rounds()

    @property
    def actual_round(self) -> Round:
        """
        Returns the current round of the tournament.
        """
        for round_obj in self.rounds:
            if round_obj.state != CLOSED:
                return round_obj
        return round_obj

    @property
    def is_in_progress(self) -> bool:
        """
        Returns True if the tournament is in progress, False otherwise.
        """
        return self.state == IN_PROGRESS

    @property
    def is_closed(self) -> bool:
        """
        Returns True if the tournament is closed, False otherwise.
        """
        return self.state == CLOSED

    @property
    def is_created(self) -> bool:
        """
        Returns True if the tournament has been created but not started, False otherwise.
        """
        return self.state == CREATED

    @property
    def players_to_complete(self) -> bool:
        """
        Returns True if there are still players needed to complete the tournament, False otherwise.
        """
        return len(self.players) < self.number_of_players

    def init_rounds(self):
        if self.id is None:
            rounds = []
            for i in range(self.number_of_rounds):
                round_num = i + 1
                round_obj = Round(round_num)
                rounds.append(round_obj)
            self.rounds = rounds

    def contains(self, player_id: int) -> bool:
        """Check if a player with the given ID is in the tournament.

        Args:
            player_id (int): The ID of the player to check.

        Returns:
            bool: True if the player is in the tournament, False otherwise.
        """
        for player in self.players:
            if player["Players"].id == player_id:
                return True
        return False

    def start(self, value: str = datetime.now().strftime("%d-%m-%Y")) -> bool:
        if self.is_created:
            self.state = IN_PROGRESS
            self.begin_date = value
            return True
        return False

    def close(self, value: str = datetime.now().strftime("%d-%m-%Y %H:%M")) -> bool:
        if self.is_in_progress and all(round.is_closed for round in self.rounds):
            self.end_date = value
            self.state = CLOSED
            return True
        return False
