# -*- coding: utf-8 -*-
from models.player import Player


MSG_PLAYER_WON = "Joueur {id} gagnant."
MSG_DRAW_MATCH = "Egalité."
MSG_SCORES_NOT_SET_YET = "Score non saisi !"


class Match:
    """
    Represents a chess match between two players.

    Attributes:
        players (dict): A dictionary with the players, keyed by the color they play ('White' or 'Black').
        scores (dict): A dictionary with the scores of each player, keyed by the color they play ('White' or 'Black').
    """

    def __init__(self, player_w: Player, player_b: Player):
        """
        Initializes a new chess match.

        Args:
            player_w (Player): The player playing with the white pieces.
            player_b (Player): The player playing with the black pieces.
        """
        self.players = {"White": player_w, "Black": player_b}
        self.scores = {"White": 0, "Black": 0}

    @property
    def done(self) -> bool:
        """
        bool: Indicates whether the match has finished (i.e., whether the scores have been set).
        """
        return sum(self.scores.values()) > 0

    @property
    def comment(self):
        """
        str: A message summarizing the result of the match, based on the scores.
        """
        if not self.done:
            return MSG_SCORES_NOT_SET_YET
        if self.scores["White"] > self.scores["Black"]:
            return MSG_PLAYER_WON.format(id=self.players["White"].id)
        elif self.scores["White"] < self.scores["Black"]:
            return MSG_PLAYER_WON.format(id=self.players["Black"].id)
        else:
            return MSG_DRAW_MATCH

    @property
    def result(self):
        """
        dict: A dictionary with the scores of each player, keyed by the color they play ('White' or 'Black').
        """
        return self.scores

    def set_result(self, score_w, score_b):
        self.scores["White"] = score_w
        self.scores["Black"] = score_b

    def won(self, color="White"):
        """
        Sets the score of the given color to 1 and the other to 0.

        Args:
            color (str): The color of the player who won ('White' or 'Black'). Defaults to 'White'.
        """
        if color == "White":
            self.set_result(1, 0)
        elif color == "Black":
            self.set_result(0, 1)

    def draw(self):
        """
        Sets the scores of both players to 0.5
        """
        self.set_result(0.5, 0.5)
