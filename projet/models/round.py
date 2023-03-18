from datetime import datetime
from models.match import Match

CREATED = 'Create'
PREPARED = 'Prepared'
IN_PROGRESS = 'In progress'
CLOSED = 'Closed'


class Round:
    """
    Represents a round of matchs in a tournament.

    Attributes:
        round_number (int): The number of the round.
        matchs (list): A list of Match objects in the round.
        state (str): The current state of the round (Created, In Progress, or Closed).
        begin_date (str): The date and time the round began (in the format '%d-%m-%Y %H:%M').
        end_date (str): The date the round ended (in the format '%d-%m-%Y').
    """

    def __init__(self, round_number=1):
        self.round_number = round_number
        self.state = CREATED
        self.begin_date = ""
        self.end_date = ""
        self.matchs: list[Match] = []

    @property
    def name(self):
        return f"Round {self.round_number}"

    @property
    def is_in_progress(self):
        return self.state == IN_PROGRESS

    @property
    def is_closed(self):
        return self.state == CLOSED

    @property
    def is_created(self):
        return self.state == CREATED

    @property
    def is_prepared(self):
        return self.state == PREPARED

    def prepare(self):
        self.state = PREPARED

    def start(self):
        """
        Starts the round and sets the begin_date attribute.

        Args:
            value (str): The date and time the round began (in the format '%d-%m-%Y %H:%M').

        Returns:
            str: 'Started Now' if the round is successfully started, IN_PROGRESS if the round is already in progress,
            CLOSED if the round has already ended, and False otherwise.
        """
        if self.is_prepared:
            self.state = IN_PROGRESS
            self.begin_date = datetime.strftime(
                datetime.now(), "%d-%m-%Y %H:%M")
            return True
        return False

    def close(self):
        """
        Closes the round and sets the end_date attribute.

        Args:
            value (str): The date the round ended (in the format '%d-%m-%Y').

        Returns:
            str: 'Closed Now' if the round is successfully closed, CREATED if the round has not been started yet,
            CLOSED if the round has already ended, and False otherwise.
        """
        if self.is_in_progress and all(match.done for match in self.matchs):
            self.end_date = datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M")
            for match in self.matchs:
                match.players["White"].rank += match.scores["White"]
                match.players["Black"].rank += match.scores["Black"]
            self.state = CLOSED
            return True
        return False
