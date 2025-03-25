class Team():
    def __init__(self):
        """
        Initializes a baseball team with a name, players, and a score.
        Attributes:
            name (str): The name of the team.
            players (list): A list of players on the team.
            wins (int): The number of wins the team has.
            losses (int): The number of losses the team has.
            wpct (float): The winning percentage of the team.
            streak (int): The current winning or losing streak of the team.
        """
        self.name = None
        self.players = []
        self.wins = 0
        self.losses = 0
        self.wpct = 0.0
        self.streak = 0
