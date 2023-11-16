"""File to define Fish class."""


class Fish:
    """This class defines a object called 'Fish'."""
    age: int

    def __init__(self):
        """This method defines the attribute of a Fish."""
        self.age = 0

    def one_day(self):
        """This method increases the age atrribute of a Fish for every day that passes."""
        self.age += 1