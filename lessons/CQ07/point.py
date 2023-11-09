"""Challenge question for Classes Lesson."""
from __future__ import annotations


class Point: 
    """This is my class to define a point with attribute x and y."""
    x: float
    y: float

    def __init__(self, x_init: float = 0, y_init: float = 0) -> None:
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Updates the existing point by a factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Create a new point scaled by a factor."""
        new_point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __mul__(self, factor: int | float) -> Point:
        """Overrides multiplication operator."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, factor: int | float) -> Point:
        """Overrides addition operator."""
        return Point(self.x + factor, self.y + factor)
    
    def __str__(self) -> str:
        """Overloads the str method."""
        return f"x: {self.x}; y: {self.y}"