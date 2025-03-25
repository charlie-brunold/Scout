class League:
    """
    A class to represent a baseball league.
    """

    def __init__(self, name):
        """
        Initializes a League object with the given name.

        Args:
            name (str): The name of the league.
        """
        self.name = name

    def __str__(self):
        """
        Returns a string representation of the League object.

        Returns:
            str: A string representation of the League object.
        """
        return self.name