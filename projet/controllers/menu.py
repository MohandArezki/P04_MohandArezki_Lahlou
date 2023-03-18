from controllers.player import PlayerController
from controllers.tournament import TournamentController
from views.menu import Menu

player_ctrl = PlayerController()
tournament_ctrl = TournamentController()


def menu_round_management():
    """
    Displays a menu to manage the currently selected tournament.
    """
    title = f"<<- {tournament_ctrl.tournament.name} ->>"
    menu = Menu(title)
    menu.add_item("1", "Appairage des joueurs de la ronde", tournament_ctrl.pairing)
    menu.add_item("2", "Démarrer la ronde", tournament_ctrl.start_round)
    menu.add_item("3", "Saisie des scores", tournament_ctrl.set_score)
    menu.add_item("4", "Terminer la ronde", tournament_ctrl.close_round)
    menu.add_item("5", "Quitter le menu", is_exit_option=True)
    menu.run()


def menu_tournament_management():
    """
    Displays a menu to manage the currently selected tournament.
    """
    tournament_ctrl.select_tournament()
    if not tournament_ctrl.tournament:
        return
    title = f"<<- {tournament_ctrl.tournament.name} ->>"
    menu = Menu(title)
    menu.add_item("1", "Mise à jour", tournament_ctrl.update_tournament)
    menu.add_item("2", "Séléction de Joueurs", tournament_ctrl.select_players)
    menu.add_item("3", "Démarrer le Tournoi", tournament_ctrl.start_tournament)
    menu.add_item("4", "Gestion de la ronde en cours.", menu_round_management)
    menu.add_item("5", "Terminer le Tournois", tournament_ctrl.close_tournament)
    menu.add_item("6", "Classement des participants", tournament_ctrl.show_tournament)
    menu.add_item("7", "Quitter le menu", is_exit_option=True)
    menu.run()


def menu_reports():
    """
    Displays a menu to generate reports related to players and tournaments.
    """
    menu = Menu("Rapports")
    menu.add_item("1", "Liste des Jouueurs / Ordre Alphabétique", player_ctrl.show_all_players_by_fullname)
    menu.add_item("2", "Liste des Joueursr / Classement", player_ctrl.show_all_players_by_rank)
    menu.add_item("3", "Liste de tous les tournois", tournament_ctrl.show_all_tournaments)
    menu.add_item("4", "Quitter le menu", is_exit_option=True)
    menu.run()


def menu_tournaments():
    """
    Displays a menu to manage tournaments.
    """
    menu = Menu("Les Tournois")
    menu.add_item("1", "Création", tournament_ctrl.add_tournament)
    menu.add_item("2", "Gestion d'un Tournoi", menu_tournament_management)
    menu.add_item("3", "Quitter le menu", is_exit_option=True)
    menu.run()


def menu_players():
    """
    Displays a menu to manage players.
    """
    menu = Menu("Gestion des Joueurs")
    menu.add_item("1", "Création", player_ctrl.add_player)
    menu.add_item("2", "Modification", player_ctrl.update_player)
    menu.add_item("3", "Quitter le menu", is_exit_option=True)
    menu.run()


def menu_main():
    """
    Displays the main menu for the application.
    """
    menu = Menu("Gestion des Tournois d'échecs")
    menu.add_item("1", "Joueurs", menu_players)
    menu.add_item("2", "Tournois", menu_tournaments)
    menu.add_item("3", "Rapports", menu_reports)
    menu.add_item("4", "Quitter le menu", is_exit_option=True)
    menu.run()
