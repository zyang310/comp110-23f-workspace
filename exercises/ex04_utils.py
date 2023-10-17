"""Using list to do things."""

__author__ = "730713735"


def all(int_list: list[int], number: int) -> bool:
    """This function tells us if a number is in a list or not."""
    counter: int = 0
    switch: int = 0
    if len(int_list) == 0:
        return False
    while counter < len(int_list):
        if number == int_list[counter]:
            switch += 1
        counter += 1
    if switch == counter:
        return True
    else:
        return False


def max(int_list: list[int]) -> int:
    """This function gives us the biggest number in a list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    counter: int = 1
    max_num: int = int_list[0]
    while counter < len(int_list):
        if int_list[counter] > max_num:
            max_num = int_list[counter]
        counter += 1
    return int(max_num)


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """This function tells us if the two list are the same or not."""
    counter: int = 0
    length: int = len(int_list1)
    compare: int = 0
    if len(int_list1) != len(int_list2):
        return False
    while counter < len(int_list1):
        if int_list1[counter] == int_list2[counter]:
            compare += 1
        counter += 1
    if compare == length:
        return True
    else:
        return False