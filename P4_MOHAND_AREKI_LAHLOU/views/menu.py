from console.utils import wait_key
from controllers.database import Database
from models.menu import Menu
from views.player import PlayerView
from views.tournament import TournamentView


class MenuView:

    def root():
        mainMenu = Menu("Club d'Echecs")
        mainMenu.add('1] - Gérer les Joueurs', MenuView.players)
        mainMenu.add('2] - Gérer les Tournois', MenuView.tournaments)
        mainMenu.run()

    def players():
        playersMenu = Menu("Gestion des Joueurs")
        playersMenu.add('1] - Créer un nouveau Joueur', PlayerView.create_player)
        playersMenu.add('2] - Editer un joueur', PlayerView.edit_player)
        playersMenu.add('3] - Rapports', MenuView.playersRepports)
        playersMenu.run()

    def playersRepports():
        playerRepportsMenu = Menu("Gestion des Joueurs / Rapports")
        # playerRepportsMenu.add('1] - Définir un Filtre ', Database.load)
        playerRepportsMenu.add('1] - Liste des joueurs tirée par Code INE', PlayerView.show_players_by_INE)
        playerRepportsMenu.add('2] - Liste des joueurs tirée par Nom Et prénom', PlayerView.show_players_by_FL)
        playerRepportsMenu.add('3] - Liste des joueurs tirée par Rang Et Score', PlayerView.show_players_by_RS)
        playerRepportsMenu.run()

    def tournaments():
        tournamentsMenu = Menu("Gestion des Tournoi")
        tournamentsMenu.add('1] - Créer un nouveau tournoi', TournamentView.create_tournament)
        tournamentsMenu.add('2] - Editer un Tournoi', TournamentView.edit_tournament)
        tournamentsMenu.add('3] - Rapports', TournamentView.show_Tournament)
        tournamentsMenu.run()
