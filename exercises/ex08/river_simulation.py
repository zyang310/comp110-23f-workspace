"""This File uses creates a instance of the class 'River' and calls the method that starts the simulation."""
from exercises.ex08.river import River


my_river: River = River(10, 2)
my_river.view_river()
my_river.one_river_week()