"""Combining two lists into a dictionary."""

__author__ = "730713735"


def zip(str_list: list[str], num_list: list[int]) -> dict[str, int]:
    """This functions put together key value from two list."""
    dictionary: dict[str, int] = dict()
    counter: int = 0
    if len(num_list) != len(str_list) or len(num_list) == 0:
        return dictionary
    for string in str_list:
        dictionary[string] = num_list[counter]
        counter += 1
    return dictionary