# -*- coding: utf-8 -*-
import random
from models.tournament import Tournament, BLITZ, RAPID, BULLET
from models.match import Match
from controllers.player import PlayerController
from repositories.tournament import TournamentRepository
from views.tournament import TournamentView

TIME_CONTROL_CHOICES = [BLITZ, RAPID, BULLET]

MSG_LISTE_ID = "Liste des Tournois par ID"

MSG_ID = "ID du tournoi : "
MSG_NOT_FOUND = "Tournoi non trouvé!"
MSG_CREATE_NAME = "Nom : "
MSG_CREATE_LOCATION = "Lieu : "
MSG_CREATE_TIME_CONTROLE = "Conrôle du temps (B)'Bullet', (Z)'Blitz', (R)'Rapid'  : "
MSG_CREATE_DESCRIPTION = "Description : "
MSG_CREATE_NUMBER_PLAYERS = "Nombre de participants : "
MSG_CREATE_NUMBER_ROUNDS = "Nombre de rondes : "

MSG_KEEP_ACTUAL_VALUES = " -- Appuyer sur Entrée pour garder les valeurs actuelles --"
MSG_UPDATE_NAME = "Nom [{}]: "
MSG_UPDATE_LOCATION = "Lieu [{}]: "
MSG_UPDATE_TIME_CONTROLE = "Conrôle de temps [{}] (B)'Bullet', (Z)'Blitz', (R)'Rapid' : "
MSG_UPDATE_NUMBER_PLAYERS = "Nombre de participants [{}]: "
MSG_UPDATE_NUMBER_ROUNDS = "Nombre de rondes [{}]: "
MSG_UPDATE_DESCRIPTION = "Description [{}]: "

MSG_ADD_PLAYER = "Ajouter un autre joueur ? [O] (O/N) : "
MSG_SELECT_PLAYER = "Sélectionner un joueur dans cette liste"
MSG_LIST_TO_COMPLETE = "Completer la liste des participants.({}) enregistrés."
MSG_LIST_COMPLETE = "la liste est compléte."
MSG_ID_PLAYER = "ID du joueur {} : "
MSG_CANCELLED = "Opération annulée."
MSG_CONFIRM = "Valider l'opération ? [O] (O/N) : "
MSG_DONE = "Données enregistrées dans la BDD."

MSG_CLOSED = "Le tournoi est terminé."
MSG_TOURNAMENT_IN_PROGRESS = "le tournoi est en cours."
MSG_TOURNAMENT_START = "Démarrer le tournoi ?[O] (O/N) : "
MSG_TOURNAMENT_CLOSE = "Terminer le tournoi ?[O] (O/N) : "
MSG_TOURNAMENT_STARTED = "Tournoi en cours...."
MSG_NOT_STARTED_YET = "Le tournoi n'a pas encore démarré."

MSG_ROUND_IN_PROGRESS = "la ronde est en cours..."
MSG_ROUND_START = "Démarrer la ronde ?[O] (O/N) : "
MSG_ROUND_CLOSE = "Terminer la ronde ?[O] (O/N) : "
MSG_ROUND_STARTED = "Ronde démarrée."
MSG_ROUND_NOT_STARTED_YET = "Ronde non démarré."
MSG_ROUND_CLOSED = "Ronde Términée"
MSG_ROUND_START = "Démarrer la ronde ?[O] (O/N) : "
MSG_ROUND_PARING_NOT_DONE = "Appairage des joueurs non effectué."
MSG_SET_SCORE = "Score [{}] (B) Blanc Gagnant // (R) Noir Gagnant // (E) Egalité : "
MSG_AN_OTHER_SCORE = "Saisir le score du match suivant ? [O] O/N "


class TournamentController:
    """Class that handles user interactions and manages tournaments."""

    def __init__(self) -> None:
        """Initializes a new instance of the TournamentController class.

        This constructor creates a new instance of the TournamentRepository class and
        a new instance of the TournamentView class, and sets the `tournament` attribute to None.

        Args:
            None

        Returns:
            None
        """
        self.players_ctrl = PlayerController()
        self.repository = TournamentRepository()
        self.view = TournamentView()
        self.tournament = None

    def show_all_tournaments(self) -> None:
        """Displays all tournaments in the repository.

        This function retrieves all tournaments from the repository, sorts them by ID,
        and displays them using the `display_tournaments()` method of the view class.

        Args:
            None

        Returns:
            None
        """
        tournaments = self.repository.get_all_tournaments()
        tournaments.sort(key=lambda x: x.id)
        self.view.display_tournaments(tournaments, MSG_LISTE_ID)

    def show_tournament(self) -> None:
        """Displays the details of a selected tournament.

        This function first calls the `select_tournament()` method to retrieve a tournament
        from the repository based on user input. If a tournament is found, it is passed to
        the `display_tournament()` method of the view to display its details.

        """
        if self.tournament:
            self.view.display_tournament(self.tournament)

    def select_tournament(self):
        """Prompts the user to select a tournament by ID and retrieves it from the repository.

        This function prompts the user to input a tournament ID, retrieves the corresponding
        tournament from the repository, and sets the `tournament` attribute to the selected
        tournament.

        If the tournament is not found, a message is displayed and the function returns.

        Args:
            None

        Returns:
            None
        """
        id = self.view.prompt_input_int(MSG_ID, None)
        tournament = self.repository.get_tournament(id)
        if not tournament:
            self.view.message(MSG_NOT_FOUND)
            return
        self.tournament = tournament

    def add_tournament(self):
        """Adds a new tournament to the repository.

        This function prompts the user to input the necessary information for a new tournament,
        creates a new `Tournament` object with the input data, and adds it to the repository.

        Args:
            None

        Returns:
            None
        """
        name = self.view.prompt_input_str(MSG_CREATE_NAME)
        location = self.view.prompt_input_str(MSG_CREATE_LOCATION)
        time_control = self.view.prompt_input_choice(
            MSG_CREATE_TIME_CONTROLE, TIME_CONTROL_CHOICES)
        number_of_players = self.view.prompt_input_int(
            MSG_CREATE_NUMBER_PLAYERS)
        number_of_rounds = self.view.prompt_input_int(MSG_CREATE_NUMBER_ROUNDS)
        description = self.view.prompt_input_str(MSG_CREATE_DESCRIPTION)
        tournament = Tournament(
            name, location, time_control, description, number_of_players, number_of_rounds)

        if self.view.confirm(MSG_CONFIRM):
            self.repository.add_tournament(tournament)
            self.view.message(MSG_DONE)
        else:
            self.view.message(MSG_CANCELLED)

    def update_tournament(self):
        """Updates the information of a selected tournament.

        If no tournament is selected, this method does nothing. Otherwise, it prompts the
        user to update the tournament's name, location, time control, number of players
        (if the tournament is in the CREATED state), number of rounds (if the tournament is in
        the CREATED state), and description. It then updates the tournament in the repository and displays
        a success message if the user confirms, or a cancellation message otherwise.
        """
        if self.tournament is None:
            return

        print(MSG_KEEP_ACTUAL_VALUES)
        messages = {'name': MSG_UPDATE_NAME.format(self.tournament.name),
                    'location': MSG_UPDATE_LOCATION.format(self.tournament.location),
                    'time_control': MSG_UPDATE_TIME_CONTROLE.format(self.tournament.time_control),
                    'description': MSG_UPDATE_DESCRIPTION.format(self.tournament.description),
                    'number_of_players': MSG_UPDATE_NUMBER_PLAYERS.format(self.tournament.number_of_players),
                    'number_of_rounds': MSG_UPDATE_NUMBER_ROUNDS.format(self.tournament.number_of_rounds)}
        defaults = {'name': self.tournament.name,
                    'location': self.tournament.location,
                    'time_control': self.tournament.time_control,
                    'description': self.tournament.description,
                    'number_of_players': self.tournament.number_of_players,
                    'number_of_rounds': self.tournament.number_of_rounds}
        self.tournament.name = self.view.prompt_input_str(
            messages['name'], defaults['name'])
        self.tournament.location = self.view.prompt_input_str(
            messages['location'], defaults['location'])
        self.tournament.time_control = self.view.prompt_input_choice(
            messages['time_control'], TIME_CONTROL_CHOICES, defaults['time_control'])
        self.tournament.description = self.view.prompt_input_str(
            messages['description'], defaults['description'])
        if self.tournament.is_created:
            self.tournament.number_of_players = self.view.prompt_input_int(
                messages['number_of_players'], defaults['number_of_players'])
            self.tournament.number_of_rounds = self.view.prompt_input_int(
                messages['number_of_rounds'], defaults['number_of_rounds'])

        if self.view.confirm(MSG_CONFIRM):
            self.repository.update_tournament(self.tournament)
            self.view.message(MSG_DONE)
        else:
            self.view.message(MSG_CANCELLED)

    def start_tournament(self):
        """
        Starts a tournament if it is not already in progress or closed.
        """
        if self.tournament is None:
            self.view.message(MSG_NOT_FOUND)
            return

        if self.tournament.is_in_progress:
            self.view.message(MSG_TOURNAMENT_IN_PROGRESS)
            return

        if self.tournament.is_closed:
            self.view.message(MSG_CLOSED)
            return

        if self.tournament.players_to_complete:
            self.view.message(MSG_LIST_TO_COMPLETE.format(
                f"{len(self.tournament.players)+1} / {self.tournament.number_of_players}"))
            return

        if self.view.confirm(MSG_TOURNAMENT_START):
            self.tournament.start()
            self.repository.update_tournament(self.tournament)
            self.view.message(MSG_TOURNAMENT_STARTED)
        else:
            self.view.message(MSG_CANCELLED)

    def close_tournament(self):
        """Closes a selected tournament and updates its state in the repository."""
        if self.tournament is None:
            self.view.message(MSG_NOT_FOUND)
            return

        if self.tournament.is_created:
            self.view.message(MSG_NOT_STARTED_YET)
            return

        if self.tournament.is_closed:
            self.view.message(MSG_CLOSED)
            return

        if self.view.confirm(MSG_CONFIRM):
            self.tournament.close()
            self.repository.update_tournament(self.tournament)
            self.view.message(MSG_DONE)
        else:
            self.view.message(MSG_CANCELLED)

    def pairing(self):
        if self.tournament is None:
            self.view.message(MSG_NOT_FOUND)
            return
        if self.tournament.is_closed:
            self.view.message(MSG_CLOSED)
            return
        if self.tournament.is_created:
            self.view.message(MSG_NOT_STARTED_YET)
            return
        if self.tournament.actual_round.is_in_progress:
            self.view.message(MSG_ROUND_IN_PROGRESS)
            return

        if self.view.confirm(MSG_CONFIRM):
            if self.tournament.actual_round.round_number == 1:
                matchs = []
                random.shuffle(self.tournament.players)
                player = 0
                while player < self.tournament.number_of_players:
                    match = Match(
                        self.tournament.players[player], self.tournament.players[player+1])
                    player += 2
                    matchs.append(match)
                self.tournament.actual_round.matchs = matchs
            else:
                matchs = []
                self.tournament.players.sort(key=lambda x: x.rank, reverse=True)
                middle = len(self.tournament.players) // 2
                players_w = self.tournament.players[:middle]
                players_b = self.tournament.players[middle:]
                idx = 0
                while idx < len(players_w):
                    match = Match(players_w[idx], players_b[idx])
                    idx += 1
                    matchs.append(match)
                self.tournament.actual_round.matchs = matchs

            self.tournament.actual_round.prepare()
            self.repository.update_tournament(self.tournament)
            self.view.display_ronund(self.tournament)

        else:
            self.view.message(MSG_CANCELLED)

    def available_players(self):
        all_player_ids = [
            player.id for player in self.players_ctrl.select_all_players()]
        tournament_player_ids = [
            player.id for player in self.tournament.players]
        available_player_ids = set(all_player_ids) - set(tournament_player_ids)
        available_players = [self.players_ctrl.repository.get_player(
            player_id) for player_id in available_player_ids]
        return available_players

    def select_players(self):
        if self.tournament.is_in_progress:
            self.view.message(MSG_TOURNAMENT_IN_PROGRESS)
            return
        elif self.tournament.is_closed:
            self.view.message(MSG_CLOSED)
            return
        if not self.tournament.players_to_complete:
            self.view.message(MSG_LIST_COMPLETE)
            return
        tournament = self.tournament
        while self.tournament.players_to_complete:
            players_inserted_str = f"{len(self.tournament.players)+1} / {self.tournament.number_of_players}"
            available_players = self.available_players()
            self.players_ctrl.view.display_players(
                available_players, MSG_SELECT_PLAYER, False)
            player_ids = [str(player.id) for player in available_players]
            selected_id = self.view.prompt_input_choice(
                MSG_ID_PLAYER.format(players_inserted_str), player_ids)
            selected_player = self.players_ctrl.repository.get_player(
                int(selected_id))
            self.tournament.players.append(selected_player)
            if not self.view.confirm(MSG_ADD_PLAYER):
                break
        if self.view.confirm(MSG_CONFIRM):
            self.repository.update_tournament(self.tournament)
            self.view.message(MSG_DONE)
        else:
            self.tournament = tournament
            self.view.message(MSG_CANCELLED)

    def start_round(self):
        if self.tournament.actual_round.is_in_progress:
            self.view.message(MSG_ROUND_IN_PROGRESS)
            return
        if self.tournament.actual_round.is_created:
            self.view.message(MSG_ROUND_PARING_NOT_DONE)
            return
        if self.view.confirm(MSG_ROUND_START):
            self.tournament.actual_round.start()
            self.repository.update_tournament(self.tournament)
            self.view.message(MSG_ROUND_STARTED)
        else:
            self.view.message(MSG_CANCELLED)

    def close_round(self):
        if self.tournament.actual_round.is_created or self.tournament.actual_round.is_prepared:
            self.view.message(MSG_ROUND_NOT_STARTED_YET)
            return
        if self.view.confirm(MSG_ROUND_CLOSE):
            self.tournament.actual_round.close()
            self.repository.update_tournament(self.tournament)
            self.view.message(MSG_ROUND_CLOSED)
        else:
            self.view.message(MSG_CANCELLED)

    def set_score(self):
        input(self.tournament.actual_round.state)
        if self.tournament.actual_round.is_in_progress:
            tournamant = self.tournament
            i = 1
            while i <= len(self.tournament.actual_round.matchs):
                match = self.tournament.actual_round.matchs[i-1]
                players = f"{match.players['White'].id})- {match.players['White'].fullname} \
    (Blanc) Vs {match.players['Black'].id})- {match.players['Black'].fullname} (Noir)"
                score = self.view.prompt_input_choice(MSG_SET_SCORE.format(players), ['B', 'N', 'E'])
                if score == 'E':
                    match.draw()
                elif score == 'B':
                    match.won('White')
                else:
                    match.won('Black')
                self.tournament.actual_round.matchs[i-1] = match
                if not self.view.confirm(MSG_AN_OTHER_SCORE):
                    break
                i += 1
            if self.view.confirm(MSG_CONFIRM):
                self.repository.update_tournament(self.tournament)
                self.view.message(MSG_DONE)
            else:
                self.tournament = tournamant
                self.view.message(MSG_CANCELLED)
