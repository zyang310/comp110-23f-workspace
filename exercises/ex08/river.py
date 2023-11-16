"""File to define River class."""

__author__ = "730713735"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """This class defines a object called 'River'."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """This methods checks the age of Bears and Fish and remove them from the list of Bears and Fish if they go pass a certain age."""
        new_bear_list = []
        for each_bear in self.bears:
            if each_bear.age <= 5:
                new_bear_list.append(each_bear)
        self.bears = new_bear_list
        new_fish_list = []
        for each_fish in self.fish:
            if each_fish.age <= 3:
                new_fish_list.append(each_fish)
        self.fish = new_fish_list

    def bears_eating(self):
        """This method checks if the each bear has five fishes, if yes, the bears eats and fishes are removed from the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self):
        """This method checks if a bear's hunger go below zero, if yes then the bear is removed from the river."""
        bear_hunger: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                bear_hunger.append(i)
        self.bears = bear_hunger
        
    def repopulate_fish(self):
        """This method spawns 4 fish for every pair of fish in the river."""
        babies: int = (len(self.fish) // 2) * 4
        for i in range(babies):
            self.fish.append(Fish()) 

    def repopulate_bears(self):
        """This method spawns 1 bear for every pair of bears in the river."""
        babies: int = len(self.bears) // 2
        for i in range(babies):
            self.bears.append(Bear()) 

    def remove_fish(self, amount: int) -> None:
        """This method remove a certain amount of fish from the river."""
        for i in range(0, amount):
            self.fish.pop(0)
    
    def view_river(self) -> None:
        """This method prints out the current day the river simulation is on."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self) -> None:
        """This method simulates a whole week of river."""
        for i in range(0, 7):
            self.one_river_day()