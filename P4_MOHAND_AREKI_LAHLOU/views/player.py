import tabulate
from models.player import Player 
from controllers.database import Database
import json


class PlayerViews:
    """ Player views
        A class for CRUD operations 
    """

    def show_players(key:int=0):
       table = Database.tb_players.all()
       if key == 0:  # we sort the list by Fisrtname and LastName
            print("List of Players Sorted by INE")
            table = sorted(table, key=lambda k: (k['INE']))    
       elif key == 1: # we sort the list by Rank and Score
            print("List of Players Sorted by Rank and Score")
            table = sorted(table, key=lambda k: (k['Rank'],k['Score']))    
       elif key == 2: # we sort the list by Fisrtname and Lastname
            print("List of Players Sorted by Fisrtname and Lastname")
            table = sorted(table, key=lambda k: (k['Firstname'],k['Lastname']))

       header = table[0].keys()
       rows =  [row.values() for row in table]
       print(tabulate.tabulate(rows, header, tablefmt='rst'))

    
    def delete_player(self,ine:str):
        """
        ask for INE
        search in table
        if found 
            delete
            return "Player deleted"
        else
            error 
            retrun "player not found"        
        """
        pass

    def show_player(self,ine:str):
        """ search a player using INE and show 
            - firstname 
            - lastname 
            - Rank
            - Score
        """
        pass

    def add_player(self):
        """
        Ask for data 
        INE , Fisrtname, lastname, Rank,...
        """
        pass

