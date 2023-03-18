# -*- coding: utf-8 -*-
import os
from prettytable import PrettyTable
from views.view import BaseView

MSG_CONFIRM = "Exporter le résulat dans un fichier ?[N] (O/N) : "


class TournamentView(BaseView):
    @staticmethod
    def display_tournaments(tournaments, title_msg):
        """
        Displays a table of tournaments with their details.

        Args:
            tournaments (list): A list of Tournament objects to display.
            title_msg (str): The message to display as the title of the table.
        """
        os.system('cls||clear')
        # Create a PrettyTable object with the desired fields.
        tab = PrettyTable()
        tab.field_names = ["ID",
                           "Tournoi",
                           "Lieu du déroulement de la compétition",
                           "Joeurs",
                           "Rondes",
                           "Période",
                           "Status",
                           "Description"
                           ]
        # Set the alignment and maximum width for some of the columns.
        tab.align["Tournoi"] = "l"
        tab.align["Lieu du déroulement de la compétition"] = "l"
        tab.align["Description"] = "l"
        tab.max_width["Tournoi"] = 30
        tab.max_width["Lieu du déroulement de la compétition"] = 30
        tab.max_width["Description"] = 30
        tab.clear_rows()
        # Add a row for each tournament.
        for tournament in tournaments:
            tab.add_row([tournament.id,
                         tournament.name,
                         tournament.location,
                         tournament.number_of_players,
                         tournament.number_of_rounds,
                         f"{tournament.begin_date} / {tournament.end_date}",
                         tournament.state,
                         tournament.description
                         ])
        # Print the table with the given title message.
        print(tab.get_string(title=title_msg))
        # If the user confirms to export the table to a file, call the export method.
        if TournamentView.confirm(MSG_CONFIRM, "N"):
            TournamentView.export(title_msg, [tab])

    @staticmethod
    def display_tournament(tournament):
        os.system('cls||clear')
        tab_tournament = PrettyTable()
        tab_players = PrettyTable()
        tab_rounds = PrettyTable()
        tab_matchs = PrettyTable()

        tab_tournament.field_names = ["ID",
                                      "Lieu du déroulement de la compétition",
                                      "Joueurs",
                                      "Rondes",
                                      "Période",
                                      "Status",
                                      "Description"
                                      ]
        tab_tournament.align["Lieu du déroulement de la compétition"] = "l"
        tab_tournament.align["Description"] = "l"
        tab_tournament.max_width["Lieu du déroulement de la compétition"] = 60
        tab_tournament.max_width["Description"] = 50

        tab_players.field_names = ["ID", "Nom Et Prénom", "Né(e) le", "Genre", "Classement"]
        tab_players.align["Nom Et Prénom"] = "l"
        tab_players.min_width["Nom Et Prénom"] = 56

        tab_tournament.clear_rows()
        tab_tournament.add_row([tournament.id,
                                tournament.location,
                                tournament.number_of_players,
                                tournament.number_of_rounds,
                                f"{tournament.begin_date} / {tournament.end_date}",
                                tournament.state,
                                tournament.description
                                ])

        players_title = f"Participants enregistrés {len(tournament.players)}/{tournament.number_of_players}"
        tab_players.clear_rows()
        for player in tournament.players:
            tab_players.add_row([player.id,
                                 player.fullname,
                                 player.date_of_birth,
                                 player.gender,
                                 player.rank
                                 ])
        tournament_title = f"Tournoi [ {tournament.name} ] Ronde Actuelle [{tournament.actual_round.round_number}]"
        print(tab_tournament.get_string(title=tournament_title))
        print(tab_players.get_string(title=players_title))
        tab_rounds.field_names = ["Ronde",
                                  "De",
                                  "Au",
                                  "Status"
                                  ]
        tab_matchs.field_names = ["Blanc",
                                  "Vs",
                                  "Noir",
                                  "Commentaire"
                                  ]
        for round in tournament.rounds:
            tab_rounds.clear_rows()
            tab_rounds.min_width["Ronde"] = 44
            tab_rounds.min_width["De"] = 20
            tab_rounds.min_width["Au"] = 20
            tab_rounds.min_width["Status"] = 10

            tab_rounds.add_row([round.name,
                               round.begin_date,
                               round.end_date,
                               round.state])
            print(tab_rounds.get_string(title=f"{round.name}"))
            tab_matchs.clear_rows()
            tab_matchs.min_width["Blanc"] = 34
            tab_matchs.min_width["Noir"] = 34
            tab_matchs.min_width["Commentaire"] = 24
            tab_matchs.align["Blanc"] = "l"
            tab_matchs.align["Noir"] = "l"

            for match in round.matchs:
                tab_matchs.add_row([f"{match.players['White'].id})- {match.players['White'].fullname}",
                                   "Vs",
                                    f"{match.players['Black'].id})- {match.players['Black'].fullname}",
                                    match.comment])
            print(tab_matchs.get_string(title="Liste de matchs"))
        TournamentView.message("")
