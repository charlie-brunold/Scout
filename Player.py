class Player():
    def __init__(self, name, age, position):
        """"
        Initializes a baseball player with a name, age, and position.
        Attributes:
            name (str): The name of the player.
            age (int): The age of the player.
            position (str): The position of the player on the team.
        """
        self.name = name
        self.age = age
        self.position = position

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