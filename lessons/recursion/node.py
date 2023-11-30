"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns the data at a specific node."""
        return self.data
    
    def tail(self) -> Node | None:
        """Returns the linked list that does not include the head. Return None if the node called does not have a next."""
        return self.next
    
    def last(self) -> int:
        """This method calls on itself recursively to print out the last data of the last node in the linked list."""
        if self.next is None:
            return self.data
        return self.next.last() 