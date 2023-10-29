"""Exercises using strings."""

__author__ = "730713735"

attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the key-value pair in the dictionary."""
    dictionary: dict[str, str] = {}
    list2: list[str] = []
    counter: int = 0
    for i in given_dict:
        if given_dict[i] in list2:
            raise ValueError("Same keys if inverted")
        list2.append(given_dict[i])
    for i in given_dict:
        dictionary[list2[counter]] = i
        counter += 1
    return dictionary


def favorite_color(given_dict: dict[str, str]) -> str:
    """Returns the most popular color in given_dict."""
    frequency: dict[str, int] = {}
    for color in given_dict:
        if given_dict[color] not in frequency:
            frequency[given_dict[color]] = 1
        else:
            frequency[given_dict[color]] += 1

    largest_value: int = 0
    favorite_color: str = color
    for i in frequency:
        if frequency[i] > largest_value:
            largest_value = frequency[i]
            favorite_color = i
        
    return favorite_color


def count(given_list: list[str]) -> dict[str, int]:
    """This function returns the amount of time the each string in a list has appeared."""
    list2: list[str] = []
    dict_count: dict[str, int] = {}
    for element in given_list:
        dict_count[element] = 0
        list2.append(element)

    for element in given_list:
        if element in list2:
            dict_count[element] += 1

    return dict_count


def alphabetizer(given_list: list[str]) -> dict[str, list[str]]:
    """This functions returns a dictionary that sorts each value into a key-value pair with the key being the first letter."""
    list2: list[str] = []
    counter: int = 0
    alphabetized_dict: dict[str, list[str]] = {}
    for i in range(0, len(given_list)):
        if given_list[i][0] not in list2:
            list2.append(given_list[i][0].lower())
    
    for letter in list2:
        alphabetized_dict[letter] = []

    for letter in list2:
        for word in given_list:
            if given_list[counter][0].lower() == letter:
                alphabetized_dict[letter].append(word)
            counter += 1
        counter = 0
       
    return alphabetized_dict


def update_attendance(given_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """This functions allows the user to update a attendence sheet when given the day and student name."""
    if day not in given_log:
        given_log[day] = []
    given_log[day].append(student)
    return given_log