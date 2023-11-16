"""File to define Bear class."""


class Bear:
    """Define class 'Bear'."""
    age: int 
    hunger_score: int

    def __init__(self) -> None:
        """Define Bear attribute."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Tracks what changes happen to a bear in one day."""
        self.age = self.age + 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """This method adds 1 hunger score for every fish a bear eats."""
        self.hunger_score += num_fish