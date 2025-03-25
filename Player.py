class Player:
    def __init__(self, name, age, primary_position):
        """"
        Initializes a baseball player with a name, age, and position.
        Attributes:
            name (str): The name of the player.
            age (int): The age of the player.
            primary_position (int): The primary position of the player.
            secondary_positions (list, int): A list of secondary positions the player can play.
            player_id (str): The unique identifier for the player.
            jersey_number (int): The jersey number of the player.
            team_affiliations (list, Team): A list of teams the player has played for.
        """
        self.name = name
        self.age = age
        self.primary_position = primary_position
        self.secondary_positions = []
        self.player_id = None
        self.jersey_number = None
        self.team_affiliations = []

    def get_details(self):
        """"
        Returns the details of the player as a formatted string."
        """
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"

    def set_position(self, new_position):
        """"
        Sets a new position for the player."
        """
        self.position = new_position