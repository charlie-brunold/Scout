class GameState():
    def __init__(self):
        """"
        Initializes the game state for a baseball game simulation.
        This includes the teams, scores, current inning, half-inning,
        outs, balls, strikes, bases, batter, pitcher, and game over status.
        Attributes:
            home_team (str): The name of the home team.
            away_team (str): The name of the away team.
            home_score (int): The score of the home team.
            away_score (int): The score of the away team.
            current_inning (int): The current inning of the game.
            current_half (str): The current half of the inning ('top' or 'bottom').
            outs (int): The number of outs in the current half-inning.
            balls (int): The number of balls thrown by the pitcher.
            strikes (int): The number of strikes thrown by the pitcher.
            bases (list): A list representing the players on base.
            batter (str): The name of the current batter.
            pitcher (str): The name of the current pitcher.
            game_over (bool): Indicates if the game is over.
        """
        self.home_team = None
        self.away_team = None
        self.home_score = 0
        self.away_score = 0
        self.current_inning = 1
        self.current_half = "top"
        self.outs = 0
        self.balls = 0
        self.strikes = 0
        self.bases = [None, None, None]
        self.batter = None
        self.pitcher = None
        self.game_over = False

