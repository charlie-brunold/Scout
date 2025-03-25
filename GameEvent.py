class GameEvent:
    def __init__(self, game_id, event_time=None, event_type=None):
        """
        Initializes a game event with a unique identifier, time, and type."
        Attributes:
            event_id (str): The unique identifier for the event.
            game_id (str): The unique identifier for the game.
            event_time (str): The time of the event.
            event_type (str): The type of the event.
        """
        self.event_id = None
        self.game_id = game_id
        self.event_time = event_time
        self.event_type = event_type

    """
    Types of baseball events:
    - Pitch
    - Bunt
    - Single
    - Double
    - Triple
    - Home Run
    - Error
    - Walk
    - Intentional Walk
    - Hit by Pitch
    - Strikeout
    - Flyout
    - Groundout
    - Double Play
    - Force Out
    - Sacrifice Fly
    - Sacrifice Bunt
    - Stolen Base
    - Caught Stealing
    - Pickoff
    - Wild Pitch
    - Passed Ball
    - Balk
    - Ejection
    - Injury
    - Substitution
    - Timeout
    - Rain Delay
    - Game Over
    - Game Resumed
    """