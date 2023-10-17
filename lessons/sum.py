"""Practice using for loops and while loops."""

__author__ = "730713735"


def main() -> None:
    """Main function."""
    list_val: list[float] = [1.2, 3.5, 2.2]
    print(w_sum(list_val))
    print(f_sum(list_val))
    print(f_range_sum(list_val))


def w_sum(given_list: list[float]) -> float:
    """Add sum of list using while loop."""
    sum_list: float = 0
    idx: int = 0
    while idx < len(given_list):
        sum_list = sum_list + given_list[idx]
        idx += 1
    return sum_list
    

def f_sum(given_list: list[float]) -> float:
    """Add sum of list using for loop."""
    sum_list: float = 0
    idx: int = 0
    for val in given_list:
        sum_list = sum_list + given_list[idx]
        idx += 1
    
    return sum_list


def f_range_sum(given_list: list[float]) -> float:
    """Add sum of list using for loop with range."""
    sum_list: float = 0
    for x in range(0, len(given_list)):
        sum_list = sum_list + given_list[x]
    
    return sum_list


main()