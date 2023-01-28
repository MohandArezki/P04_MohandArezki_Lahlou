from console.utils import wait_key
from controllers.database import Database


class TournamentView:
    HEADER = "|   Tournoi                        |      Lieu            |     Du     |   Au       |     Description           |   Nbre de participants   |   Nbre Tours  |"

    def printHeader(title):
        print("-" * len(TournamentView.HEADER))
        print("|"+title.center(len(TournamentView.HEADER)-2)+"|")
        print("-" * len(TournamentView.HEADER))
        print(TournamentView.HEADER)
        print("-" * len(TournamentView.HEADER))

    def printDetail():
        for tournament in Database.tournamentsList:
            print(tournament)
        print("-" * len(TournamentView.HEADER))    
        print("Appuyez sur une touche pour continuer ...")
        wait_key()

    def show_Tournament():
        TournamentView.printHeader('Liste des Tournois')
        TournamentView.printDetail()
    
    def create_tournament():
        pass

    def edit_tournament():
        pass