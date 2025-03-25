class PlayerGameStats:
    def __init__(self, player_id, game_id):
        """"
        Initializes the player game statistics for a baseball game."
        Attributes:
            player_id (str): The unique identifier for the player.
            game_id (str): The unique identifier for the game.
            batting_stats (dict): A dictionary containing batting statistics.
            pitching_stats (dict): A dictionary containing pitching statistics.
            fielding_stats (dict): A dictionary containing fielding statistics.
            baserunning_stats (dict): A dictionary containing baserunning statistics.
            miscellaneous_stats (dict): A dictionary containing miscellaneous statistics.
        """
        self.player_id = player_id
        self.game_id = game_id
        self.batting_stats = {
            'at_bats': 0,
            'hits': 0,
            'runs': 0,
            'RBIs': 0,
            'walks': 0,
            'strikeouts': 0,
        }
        self.pitching_stats = {
            'innings_pitched': 0,
            'runs_allowed': 0,
            'strikeouts': 0,
            'walks_allowed': 0,
            'hits_allowed': 0
        }
        self.fielding_stats = {
            'errors': 0,
            'putouts': 0,
            'assists': 0
        }
        self.baserunning_stats = {
            'stolen_bases': 0,
            'caught_stealing': 0
        }
        self.miscellaneous_stats = {
            'sacrifice_flies': 0,
            'sacrifice_bunts': 0,
            'double_plays': 0
        }