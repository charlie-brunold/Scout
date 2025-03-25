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
        # pitch is a strike
            # check if pitch is a called strike
            # otherwise, pitch is a swinging strike
            # regardless, increment the strike count (helper function to check if batter strikes out)
            # if runners on base, cehck if they advance (helper function?)

        # pitch is a ball
            # ball came from a wild pitch
                # increment count and check if there is a walk (helper function)
                # if runners on base, check if they advance (helper function?)
            # ball came from a passed ball
                # increment count and check if there is a walk (helper function)
                # if runners on base, check if they advance (helper function?)

        # batter makes contact with the ball
            # check if the ball is a foul ball
            # otherwise, the ball is a hit
                # check if the ball is hard hit or weakly hit
                    # check if the ball is a ground ball  
                    # check if the ball is a line drive
                    # check if the ball is a fly ball
                    # check if the ball is a pop up



