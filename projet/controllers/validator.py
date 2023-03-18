# -*- coding: utf-8 -*-
from datetime import datetime


class Validate:
    @classmethod
    def validate_date(cls, input: str) -> bool:
        """
        Validate that a given string is a valid date in the format 'dd-mm-yyyy'.

        Args:
            input (str): The input string to validate.

        Returns:
            bool: True if the input string is a valid date, False otherwise.
        """
        try:
            datetime.strptime(input, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    @classmethod
    def validate_int(cls, input: str) -> bool:
        """
        Validate that a given string can be converted to a positive integer.

        Args:
            input (str): The input string to validate.

        Returns:
            bool: True if the input string can be converted to a positive integer, False otherwise.
        """
        try:
            if int(input) < 0:
                return False
            return True
        except Exception as err:
            print(f"error {err}")
            return False

    @classmethod
    def validate_str(cls, input: str, empty: bool = True) -> bool:
        """
        Validate that a given string is not empty or contains only whitespace.

        Args:
            input (str): The input string to validate.
            empty (bool, optional): Whether an empty string should be considered valid. Defaults to True.

        Returns:
            bool: True if the input string is not empty or contains non-whitespace characters, False otherwise.
        """
        if not empty:
            if len(input.strip()) == 0:
                return False
        return True

    @classmethod
    def validate_datetime(cls, input: str) -> bool:
        """
        Validate that a given string is a valid datetime in the format 'dd-mm-yyyy hh:mm:ss'.

        Args:
            input (str): The input string to validate.

        Returns:
            bool: True if the input string is a valid datetime, False otherwise.
        """
        try:
            datetime.strptime(input, '%d-%m-%Y %H:%M:%S')
            return True
        except Exception as err:
            print(f"error {err}")
            return False

    @classmethod
    def validate_choice(cls, input: str, options: list) -> bool:
        """
        Validate that a given string is one of the specified options.

        Args:
            input (str): The input string to validate.
            options (list): A list of valid options.

        Returns:
            bool: True if the input string is one of the valid options, False otherwise.
        """
        if Validate.validate_str(input):
            return (input.upper() in options)
        else:
            return False
