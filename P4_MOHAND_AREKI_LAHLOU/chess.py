# -*- coding: utf-8 -*-
from controllers.database import Database
from views.menu import MenuView


def main():
    Database.load()
    MenuView.root()

if __name__ == "__main__":
    main()