"""Module with math related functions and classes

Classes:
    MathClass
"""

# Ordered imports example:
# Standard libraries; first
from typing import Final

# Third-party libraries; second
import requests

# Local modules; third
from another_module import module2  # src/python_conventions/another_module/module2.py
from classModule import TestClass  # src/python_conventions/classModule.py : TestClass


class MathClass:
    """Math class with methods for adding and subtracting"""

    PI_CONSTANT: Final[float] = (
        3.1415  # A "constant" float: ALL_UPPERCASE naming convention
    )
    # (Assignment splitted to keep the line at the maximum of 88 characters (Black))

    def __init__(
        self, sent_message: str
    ) -> None:  # First argument must be self or cls; Depends on the Class
        self.sent_message: str = sent_message  # snake_case and str TypeHint
        self.sum_results: int = 0
        self.__private_variable: int = (
            21  # "Private" variable: starts with double underscore
        )

    def add(self, number1: int, number2: int) -> int:  # Docstrings as necessary
        """Adds two numbers and set the sum to the sum_results variable

        Args:
            number1 (int): First number to add
            number2 (int): Second number to add

        Returns:
            int: Sum of the equation
        """
        self.sum_results = number1 + number2
        return self.sum_results

    def subtract(self, number1: int, number2: int) -> int:
        self.sum_results = number1 - number2
        return self.sum_results

    def get_pi(self) -> float:
        """Gets the value of PI_CONSTANT which MUST be 3.1415

        Returns:
            float: The value of PI_CONSTANT.
        """
        return self.PI_CONSTANT

    def get_message(self) -> str:
        """Gets the message that was stored when this class was constructed

        Returns:
            str: The message that was stored when this class was constructed
        """
        return self.sent_message

    def get_private_variable(self) -> int:
        return self.__private_variable  # The only way to get the private variable
