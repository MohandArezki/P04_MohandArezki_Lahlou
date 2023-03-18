# -*- coding: utf-8 -*-
import os
from prettytable import PrettyTable
from views.view import BaseView

MSG_CONFIRM = "Exporter le résulat dans un fichier ?[N] (O/N) "
GENDER = ['Male', 'Female']


class PlayerView(BaseView):
    @staticmethod
    def display_players(players, title_msg, export=True):
        """
        Displays a table of players with their details.

        Args:
            players (list): A list of Player objects to display.
            title_msg (str): The message to display as the title of the table.
        """
        os.system('cls||clear')
        # Create a PrettyTable object with the desired fields.
        tab_players = PrettyTable()

        tab_players.field_names = ["ID",
                                   "Nom Et Prénom",
                                   "Date de naissance",
                                   "Genre",
                                   "Classement"
                                   ]
        # Set the alignment for the "Nom Et Prénom" column.
        tab_players.align["Nom Et Prénom"] = "l"
        tab_players.clear_rows()
        # Add a row for each player.
        for player in players:
            tab_players.add_row([player.id,
                                 player.fullname,
                                 player.date_of_birth,
                                 player.gender,
                                 player.rank
                                 ])
        # Print the table with the given title message.
        print(tab_players.get_string(title=title_msg))
        # If the user confirms to export the table to a file, call the export method.
        if export:
            if PlayerView.confirm(MSG_CONFIRM, "N"):
                PlayerView.export(title_msg, [tab_players])
