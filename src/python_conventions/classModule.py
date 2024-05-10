class TestClass:
    """
    A test class to demonstrate docstrings.

    Attributes:
        message (str): The message that will be stored in the class.

    Methods:
        get_message():
            Returns the message stored in the class instance.
    """

    def __init__(self, message: str):
        """
        Constructor for the TestClass class.

        Args:
            message (str): The message to be stored by the class instance.
        """
        self.message = message

    def get_message(self) -> str:
        """Returns the message stored in the class instance."""
        return self.message
