class Season:
    """
    A class to represent a baseball season in a given league.
    """

    def __init__(self, year, league):
        """
        Initializes a Season object with the given year and league.

        Args:
            year (int): The year of the season.
            league (League): The name of the league.
        """
        self.year = year
        self.league = league

    def __str__(self):
        """
        Returns a string representation of the Season object.

        Returns:
            str: A string representation of the Season object.
        """
        return f"{self.league} {self.year}"