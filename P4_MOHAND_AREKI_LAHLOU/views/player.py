import os
from console.utils import wait_key
from controllers.database import Database
from models.player import Player 

class PlayerView:
    HEADER = "|   INE      |      Prénom          |         Nom          |           Né(e)             | Genre      |   Rang   |   Score  |"

    def printHeader(title):  
        print("-" * len(PlayerView.HEADER))
        print("|"+title.center(len(PlayerView.HEADER)-2)+"|")
        print("-" * len(PlayerView.HEADER))
        print(PlayerView.HEADER)
        print("-" * len(PlayerView.HEADER))

    def printDetail():
        for player in Database.playersList:
            print(player)
        print("-" * len(PlayerView.HEADER))    
        print("Appuyez sur une touche pour continuer ...")
        wait_key()

    def show_players_by_INE():
        PlayerView.printHeader('Liste des joueurs triée par code INE')
        Database.playersList.sort(key=lambda x: x.ine)
        PlayerView.printDetail()

    def show_players_by_FL():
        PlayerView.printHeader("Liste des joueurs triée par Prénom Et Nom")
        Database.playersList.sort(key=lambda x: (x.firstname, x.lastname))
        PlayerView.printDetail()

    def show_players_by_RS():
        PlayerView.printHeader('Liste des joueurs triée par Rang Et Score')
        Database.playersList.sort(key=lambda x: (x.rank, x.score))
        PlayerView.printDetail()

    def create_player():
        while True:
            os.system('cls||clear')
            print("               Creation d'un nouveau joueur    ")
            ine = input("Code INE : ")
            firstname = input("Prénom   : ")
            lastname = input("Nom : ")        
            date_of_birth = input("Date de naissance : ")
            gender = input("Genre : ")
            rank = input("Rang : ")                        
            score = input("Score : ") 
            Database.insert_player(Player(ine,firstname,lastname,date_of_birth,gender,rank,score))
            wait_key()

    def edit_player():
        pass
    