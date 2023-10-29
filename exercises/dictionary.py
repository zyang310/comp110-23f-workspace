"""Exercises using strings."""

__author__ = "730713735"

attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}


def invert(given_dict: dict[str,str]) -> dict[str,str]:
    """inverts the key-value pair in the dictionary."""
    dictionary: dict[str, str] = {}
    list: list[str] = []
    counter: int = 0
    for i in given_dict:
        if given_dict[i] in list:
            raise ValueError("Same keys if inverted")
        list.append(given_dict[i])
    for i in given_dict:
        dictionary[list[counter]] = i
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
    favorite_color: str = None
    for i in frequency:
        if frequency[i] > largest_value:
            largest_value = frequency[i]
            favorite_color = i
        
    return favorite_color
    

def count(list: list[str]) -> dict[str, int]:
    """This function returns the amount of time the each string in a list has appeared."""
    list2: list[str] = []
    dict: dict[str, int] = {}
    for element in list:
        dict[element] = 0
        list2.append(element)

    for element in list:
        if element in list2:
            dict[element] += 1

    return dict


def alphabetizer(list: list[str]) -> dict[str, list[str]]:
    """This functions returns a dictionary that sorts each value into a key-value pair with the key being the first letter."""
    list2: list[str] = []
    counter: int = 0
    alphabetized_dict: dict[str, list[str]] = {}
    for i in range(0, len(list)):
        if list[i][0] not in list2:
            list2.append(list[i][0].lower())
    
    for letter in list2:
        alphabetized_dict[letter] = []

    for letter in list2:
        for word in list:
            if list[counter][0].lower() == letter:
                alphabetized_dict[letter].append(word)
            counter += 1
        counter = 0
       
    return alphabetized_dict


def update_attendence(dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """This functions allows the user to update a attendence sheet when given the day and student name."""
    if day not in dict:
        dict[day] = []
    dict[day].append(student)
    return dict