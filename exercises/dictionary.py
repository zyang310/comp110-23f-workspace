"""Exercises using strings."""

__author__ = "730713735"

def main() -> None:
    """Main function to store other functions."""
    pass


def invert(given_dict: dict[str,str]) -> dict[str,str]:
    """inverts the key-value pair in the dictionary."""
    dictionary: dict[str, str] = {}
    list = []
    counter: int = 0
    for i in given_dict:
        if given_dict[i] in list:
            raise ValueError("Same keys if inverted")
        list.append(given_dict[i])
    for i in given_dict:
        dictionary[list[counter]] = i
        counter += 1
    return dictionary


if __name__ == "__main__":
    main()