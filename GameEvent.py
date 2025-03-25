class GameEvent:
    def __init__(self, game_id, event_type=None, timestamp=None):
        """
        Initializes a game event with a unique identifier, type, and timestamp.
        
        Attributes:
            event_id (str): The unique identifier for the event.
            game_id (str): The unique identifier for the game.
            event_type (str): The type of event (e.g., pitch, hit, error).
            timestamp (datetime): The time when the event occurred.     
        """
        self.event_id = None  # Will be set when saved to database
        self.game_id = game_id # which game this event belongs to
        self.event_type = event_type
        self.timestamp = timestamp # when the event occurred
    
    def make_pitch(self, pitcher=None, batter=None, catcher=None):
        """
        Records a pitch event in the game. At this point in development, every event will happen after a pitch.
        """


