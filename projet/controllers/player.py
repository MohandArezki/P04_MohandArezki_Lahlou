# -*- coding: utf-8 -*-
from models.player import Player
from repositories.player import PlayerRepository
from views.player import PlayerView

MSG_LISTE_ID = "Liste des Joueurs par ID"
MSG_LISTE_ALPH = "Liste des joueurs par Ordre Alphabétique"
MSG_LISTE_RANK = "Liste des joueurs par Rang"

MSG_ID = "ID du Joueur : "
MSG_NOT_FOUND = "Joueur non trouvé"
MSG_CREATE_LASTNAME = "Nom : "
MSG_CREATE_FIRSTNAME = "Prénom : "
MSG_CREATE_DOB = "Date de Naissance (dd-mm--yyyy) : "
MSG_CREATE_GENDER = "Genre (M/F) : "
MSG_CREATE_RANK = "Classement : "

MSG_KEEP_ACTUAL_VALUES = " -- Appuyer sur Entrée pour garder les valeurs actuelles --"
MSG_UPDATE_LASTNAME = "Nom ({}): "
MSG_UPDATE_FIRSTNAME = "Prénom ({}): "
MSG_UPDATE_DOB = "Date de Naissance (dd-mm--yyyy) ({}): "
MSG_UPDATE_GENDER = "Genre (M/F) ({}): "
MSG_UPDATE_RANK = "Classement ({}): "

MSG_CANCELLED = "Opération annulée."
MSG_CONFIRM = "Valider l'opération ? [O] (O/N) "
MSG_DONE = "Données enregistrées dans la BDD."


class PlayerController:
    """
    A class to control player-related actions and communication with the user.

    Attributes:
        repository (PlayerRepository): An instance of the PlayerRepository class.
        view (PlayerView): An instance of the PlayerView class.
    """

    def __init__(self):
        """
        Constructs a PlayerController object with a PlayerRepository object and a PlayerView object.
        """
        self.repository = PlayerRepository()
        self.view = PlayerView()
        self.player = None

    def show_all_players_by_fullname(self):
        """
        Displays a list of all players sorted by full name.
        """
        players = self.repository.get_all_players()
        players.sort(key=lambda x: x.fullname.upper())
        self.view.display_players(
            players, MSG_LISTE_ALPH)

    def show_all_players_by_rank(self):
        """
        Displays a list of all players sorted by rank.
        """
        players = self.repository.get_all_players()
        players.sort(key=lambda x: x.rank, reverse=True)
        self.view.display_players(players, MSG_LISTE_RANK)

    def show_all_players(self):
        """
        Displays a list of all players sorted by ID.
        """
        players = self.select_all_players()
        self.view.display_players(players, MSG_LISTE_ID)

    def select_all_players(self):
        """
        Selects and returns all the players in the repository, sorted by their ID.
        """
        players = self.repository.get_all_players()
        players.sort(key=lambda x: x.id)
        return players

    def select_player(self, id):
        """
        Displays a player's information based on the ID input by the user.
        """
        player = self.repository.get_player(id)
        if not player:
            self.view.message(MSG_NOT_FOUND)
            return
        self.player = player

    def show_player(self):
        """
        Displays a player's information based on the ID input by the user.
        """
        if self.player is None:
            return
        self.view.display_player(self.player)

    def add_player(self):
        """
        Adds a new player based on user input.
        Prompts the user for the player's last name, first name, date of birth, gender, and rank.
        Uses the Player class to create a new player object with the provided information.
        Calls the repository's add_player method to add the new player to the list of players.
        """
        lastname = self.view.prompt_input_str(MSG_CREATE_LASTNAME)
        firstname = self.view.prompt_input_str(MSG_CREATE_FIRSTNAME)
        date_of_birth = self.view.prompt_input_date(MSG_CREATE_DOB)
        gender = self.view.prompt_input_choice(MSG_CREATE_GENDER, ['M', 'F'])
        rank = self.view.prompt_input_int(MSG_CREATE_RANK)
        player = Player(lastname, firstname, date_of_birth, gender, rank)
        if self.view.confirm(MSG_CONFIRM):
            self.repository.add_player(player)
            self.view.message(MSG_DONE)
        else:
            self.view.message(MSG_CANCELLED)

    def update_player(self):
        """
        Updates a player's information based on the ID input by the user.

        Prompts the user to enter the ID of the player to be updated and displays the current
        information of the player.
        The user is then prompted to enter the updated values for the player's lastname, firstname,
        date of birth, gender, and rank.
        If the user confirms the update, the player's information is updated in the repository
        and a confirmation message is displayed.
        Otherwise, a cancellation message is displayed.
        """
        id = self.view.prompt_input_int(MSG_ID, None)
        self.select_player(id)
        if self.player is None:
            return
        print(MSG_KEEP_ACTUAL_VALUES)
        self.player.lastname = self.view.prompt_input_str(
            MSG_UPDATE_LASTNAME.format(self.player.lastname), self.player.lastname)
        self.player.firstname = self.view.prompt_input_str(
            MSG_UPDATE_FIRSTNAME.format(self.player.firstname), self.player.firstname)
        self.player.date_of_birth = self.view.prompt_input_date(
            MSG_UPDATE_DOB.format(self.player.date_of_birth), self.player.date_of_birth)
        self.player.gender = self.view.prompt_input_choice(
            MSG_UPDATE_GENDER.format(self.player.gender), ['M', 'F'], self.player.gender)
        self.player.rank = self.view.prompt_input_int(MSG_UPDATE_RANK.format(self.player.rank), self.player.rank)
        if self.view.confirm(MSG_CONFIRM):
            self.repository.update_player(self.player)
            self.view.message(MSG_DONE)
        else:
            self.view.message(MSG_CANCELLED)
