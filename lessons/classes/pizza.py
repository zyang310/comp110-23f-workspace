"""Defining a Class!"""
from __future__ import annotations
"""
Think of a class definition as a "roadmap" for objects that belong to the class
You are defining the underlying structure every instance of this class will have
"""

class Pizza:
    """This is my class to represent pizza!"""
    # attributes
    # syntax <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, topping_input: int, gf_input: bool) -> None:
        """Constructor"""
        self.size = size_input
        self.toppings = topping_input
        self.gluten_free = gf_input
        # returns self

    def price(self) -> float:
        """Method to compute prince of Pizza"""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost
    
    def add_toppings(self, num_toppings: int):
        """Update existing pizza order with num_toppings"""
        self.toppings += num_toppings
    
    def add_toppings_new_orders(self, num_toppings) -> Pizza:
        """Make new pizza order using existing info"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza