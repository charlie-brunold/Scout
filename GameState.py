class GameState:
    def __init__(self):
        """"
        Initializes the game state for a baseball game simulation.
        This includes the teams, scores, current inning, half-inning,
        outs, balls, strikes, bases, batter, pitcher, and game over status.
        
        Attributes:
            teams (dict): Information about the home and away teams
            score (dict): Running score for both teams
            lineup (dict): Batting orders for both teams
            fielders (dict): Defensive positions for both teams
            game_state (dict): Current state of play (inning, outs, etc.)
            count (dict): Current ball-strike count
            bases (dict): Current baserunner situation
            active_players (dict): Current batter and pitcher
            game_metadata (dict): Metadata about the game
            game_events (list): A list of events that occurred during the game
        """
        # Team information
        self.teams = {
            "home": None,
            "away": None
        }
        
        # Score information
        self.score = {
            "home": 0,
            "away": 0,
            "by_inning": {
                "home": [],
                "away": []
            }
        }
        
        # Lineup information
        self.lineup = {
            "home": [],
            "away": [],
            "home_current_position": 0,
            "away_current_position": 0
        }
        
        # Fielder positions
        self.fielders = {
            "home": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None},
            "away": {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
        }
        
        # Current game state
        self.game_state = {
            "inning": 1,
            "half": "top",
            "outs": 0,
            "is_game_over": False
        }
        
        # Current count
        self.count = {
            "balls": 0,
            "strikes": 0
        }
        
        # Base runners
        self.bases = {
            "first": None,
            "second": None, 
            "third": None
        }
        
        # Active players
        self.active_players = {
            "batter": None,
            "pitcher": None
        }
        
        # Game metadata
        self.game_metadata = {
            "game_id": None,
            "date": None,
            "attendance": None,
            "weather": None,
            "first_pitch_time": None,
            "venue": None,
            "duration": None,
            "umpires": {
                "home": None,
                "first": None,
                "second": None,
                "third": None
            }
        }
        
        # Game events
        self.game_events = []
    
    def get_current_team_batting(self):
        """Returns the team currently batting based on the current half inning"""
        return self.teams["away"] if self.game_state["half"] == "top" else self.teams["home"]
    
    def get_current_team_fielding(self):
        """Returns the team currently fielding based on the current half inning"""
        return self.teams["home"] if self.game_state["half"] == "top" else self.teams["away"]
    
    def advance_inning(self):
        """Advances to the next half-inning, resetting outs, count, and bases as needed"""
        # Reset outs, count, and update inning/half
        self.game_state["outs"] = 0
        self.count = {"balls": 0, "strikes": 0}
        
        # If bottom half, advance to next inning
        if self.game_state["half"] == "bottom":
            self.game_state["inning"] += 1
            self.game_state["half"] = "top"
        else:
            self.game_state["half"] = "bottom"
        
        # Clear bases for new half-inning
        self.bases = {
            "first": None,
            "second": None, 
            "third": None
        }
        
        # Update current batter from lineup
        self._update_current_batter()
    
    def _update_current_batter(self):
        """Updates the current batter based on the lineup position"""
        team = "away" if self.game_state["half"] == "top" else "home"
        position = self.lineup[f"{team}_current_position"]
        self.active_players["batter"] = self.lineup[team][position]
        
        # Update the pitcher too
        opposing_team = "home" if self.game_state["half"] == "top" else "away"
        self.active_players["pitcher"] = self.fielders[opposing_team][1]  # Position 1 is pitcher
    
    def record_out(self, out_type="Generic Out"):
        """
        Records an out and advances inning if needed
        
        Args:
            out_type (str): The type of out (e.g., "Strikeout", "Flyout", "Groundout")
        
        Returns:
            dict: Updated game state information
        """
        # Create an event for this out
        event = {
            "event_type": out_type,
            "inning": self.game_state["inning"],
            "half": self.game_state["half"],
            "batter": self.active_players["batter"],
            "pitcher": self.active_players["pitcher"],
            "pre_win_probability": self.win_probability.copy(),
            "win_probability_added": 0
        }
        
        # Record the out
        self.game_state["outs"] += 1
        
        # Update player statistics
        self._update_player_stats_for_out(out_type)
        
        if self.game_state["outs"] >= 3: # if this out makes 3 outs
            # Advance to next half-inning
            self.advance_inning()
        else:
            # Reset count for next batter
            self.count = {"balls": 0, "strikes": 0}
            # Advance to next batter in lineup
            self._advance_lineup()
        
        # Update win probability after the play
        self._update_win_probability()
        event["post_win_probability"] = self.win_probability.copy()
        event["win_probability_added"] = self._calculate_wpa(event)
        
        # Add event to game events
        self.game_events.append(event)
        
        return {
            "current_state": self.get_display_state(),
            "event": event
        }
    
    def _advance_lineup(self):
        """Advances to the next batter in the lineup"""
        team = "away" if self.game_state["half"] == "top" else "home"
        self.lineup[f"{team}_current_position"] = (self.lineup[f"{team}_current_position"] + 1) % 9
        self._update_current_batter()
    
    def calculate_win_probability(self):
        """Placeholder for win probability calculation"""
        # This would be implemented with your statistical model
        return {
            "home": 0.5,  # Default 50% for home team
            "away": 0.5   # Default 50% for away team
        }