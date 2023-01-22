# -*- coding: utf-8 -*-
from models.player import Player
from controllers.database import Database

def main():

    players = Database.load_players()
    for player in players:
        print(player)

if __name__ == "__main__":
    main()