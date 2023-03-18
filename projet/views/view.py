# -*- coding: utf-8 -*-
from controllers.validator import Validate
import datetime

MSG_FILE_GENERATED = "Fichier généré.[{}]"
MSG_ERROR = "Erreur lors de la génération du fichier.{}"


class BaseView:
    @staticmethod
    def prompt_input_int(msg, default=None):
        """Prompt user for an integer input and return it."""
        repeat = True
        while repeat:
            if default is not None:
                result = input(msg) or default
            else:
                result = input(msg)
            repeat = not Validate.validate_int(result)
        return int(result)

    @staticmethod
    def prompt_input_str(msg, default=None):
        """Prompt user for a string input and return it."""
        repeat = True
        while repeat:
            if default is not None:
                result = input(msg) or default
            else:
                result = input(msg)
            repeat = not Validate.validate_str(result)

        return result

    @staticmethod
    def prompt_input_date(msg, default=None):
        """Prompt user for a date input and return it."""
        repeat = True
        while repeat:
            if default is not None:
                result = input(msg) or default
            else:
                result = input(msg)
            repeat = not Validate.validate_date(result)

        return result

    @staticmethod
    def prompt_input_datetime(msg, default=None):
        """Prompt user for a datetime input and return it."""
        repeat = True
        while repeat:
            if default is not None:
                result = input(msg) or default
            else:
                result = input(msg)
            repeat = not Validate.validate_datetime(result)

        return result

    @staticmethod
    def prompt_input_choice(msg, choices, default=None):
        """Prompt user for a choice from a list of options and return it."""
        repeat = True
        while repeat:
            if default is not None:
                result = input(msg) or default
            else:
                result = input(msg)
            repeat = not Validate.validate_choice(result, choices)

        return result.upper()

    @staticmethod
    def message(msg):
        """Display a message to the user."""
        input(f"{msg} Appuyer sur Entrée pour continuer ...")

    @staticmethod
    def confirm(msg, default="O"):
        """
        Prompt the user for confirmation and return True if the user confirms,
        False otherwise.
        """
        print()
        print("-"*len(msg))
        result = BaseView.prompt_input_choice(msg, ["O", "N"], default)
        print("-"*len(msg))
        return (result.upper() == "O")

    @staticmethod
    def export(base_filename, tables):
        """
        Export a file to the 'data/export' directory with a timestamped filename
        based on the 'base_filename' argument. Display a message to the user if
        the file was successfully generated.
        """
        try:
            filename = base_filename+datetime.datetime.now().strftime('-%d%m%Y-%H%M%S')+'.html'
            with open('data/export/'+filename, mode='w', encoding="utf-8") as w:
                for table in tables:
                    w.write(str(table)+'\n')
            BaseView.message(MSG_FILE_GENERATED.format(filename))
        except Exception as err:
            BaseView.message(MSG_ERROR.format(err))
        return
