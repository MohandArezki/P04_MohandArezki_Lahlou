import os
from views.view import BaseView


class Menu(BaseView):
    """
    A class representing a menu.
    Attributes:
        items (dict): A dictionary containing the menu items.
        title (str): The title of the menu.
    """

    def __init__(self, title):
        """
        Initializes a new instance of the Menu class.

        Args:
            title (str): The title of the menu.
        """
        self.items = {}
        self.title = title

    def add_item(self, id, name, function=None, is_exit_option=False):
        """
        Adds a new item to the menu.

        Args:
            id (int): The ID of the item.
            name (str): The name of the item.
            function (callable, optional): The function to be executed when the item is selected. Defaults to None.
            is_exit_option (bool, optional): A flag indicating if the item is an exit option. Defaults to False.
        """
        self.items[id] = {'name': name, 'function': function,
                          'is_exit_option': is_exit_option}

    def display_menu(self):
        """Displays the menu on the console."""
        os.system('cls||clear')
        print(self.title)
        print()
        for item in self.items:
            print(f"{item} - {self.items[item]['name']}")
        print()

    def run(self):
        """Runs the menu."""
        while True:
            self.display_menu()
            choice = self.prompt_input_choice(
                "Votre Choix : ", list(self.items.keys()))
            if self.items[choice]["is_exit_option"]:
                break
            self.items[choice]["function"]()
