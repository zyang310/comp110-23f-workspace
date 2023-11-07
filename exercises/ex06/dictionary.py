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
            raise KeyError("Same keys if inverted")
        list2.append(given_dict[i])
    for i in given_dict:
        dictionary[list2[counter]] = i
        counter += 1
    return dictionary


def favorite_color(given_dict: dict[str, str]) -> str:
    """Returns the most popular color in given_dict."""
    frequency: dict[str, int] = {}
    if given_dict == {}:
        return {}
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
    alphabetized_dictionary: dict[str, list[str]] = {}
    for string in given_list:
        if string.lower()[0] in alphabetized_dictionary:
            alphabetized_dictionary[string.lower()[0]].append(string)
        else:
            alphabetized_dictionary[string.lower()[0]] = [string]
    return alphabetized_dictionary
  

def update_attendance(given_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """This functions allows the user to update a attendence sheet when given the day and student name."""
    if day == ' ' or student == ' ':
        return given_log
    if day not in given_log:
        given_log[day] = []
    if student not in given_log[day]:
        given_log[day].append(student)
    return given_log