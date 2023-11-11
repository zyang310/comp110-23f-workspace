"""Testing the dictionary functions."""

__author__ = "730713735"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_empty_dictionary() -> None:
    """Test a empty dictionary."""
    assert invert({}) == {}


def test_invert_normal() -> None:
    """A normal test case."""
    dict1: dict[str, str] = {"a": "first", 'b': "second", "c": "third"}
    assert invert(dict1) == {"first": "a", "second": "b", "third": "c"}


def test_same_keyvalue() -> None:
    """Test with same key-value pair."""
    assert invert({"100": "100", "10": "10", "1": "1"}) == ({"100": "100", "10": "10", "1": "1"})


def test_same_frequency() -> None:
    """Test with same frequency of colors."""
    dictionary: dict[str, str] = {"Marc": "blue", "Ezri": "yellow", "Kris": "blue", "John": "yellow"}
    dict_answer: str = "blue"
    assert favorite_color(dictionary) == dict_answer


def test_three_color() -> None:
    """It test this function with a dictionary with three colors."""
    dict1: dict[str, str] = {"Marc": "blue", "Ezri": "green", "Kris": "blue", "John": "yellow", "Joseph": "Green", "Amy": "blue"}
    answer: str = "blue"
    assert favorite_color(dict1) == answer


def test_empty_dictionary_color() -> None:
    """Test a empty dictionary."""
    assert favorite_color({}) == {}


def test_count_empty_list() -> None:
    """Uses a empty list to test the count function."""
    given_list: list[str] = []
    assert count(given_list) == {}


def test_count_str_of_ints() -> None:
    """Given a list containing string of ints."""
    given_list: list[str] = ["1", "2", "2", "5", "5"]
    answer_dict: dict[str, int] = {'1': 1, '2': 2, '5': 2}
    assert count(given_list) == answer_dict


def test_count_normal() -> None:
    """Testing using normal list of strings."""
    given_list: list[str] = ["attempts", "attempts", "attempts", "goals", "goals"]
    answer_dict: dict[str, int] = {'attempts': 3, 'goals': 2}
    assert count(given_list) == answer_dict


def empty_alphabetizer() -> None:
    """Test if given an empty list will return an empty dictionary."""
    assert alphabetizer([]) == {}


def test_capitalized_words() -> None:
    """Test if the function still work if given a list of capitalized words."""
    given_list: list[str] = ["APPLE", "BAT", "CATTLE", "AIRPLANE", "CORN"]
    answer_dict: dict[str, list[str]] = {'a': ['APPLE', 'AIRPLANE'], 'b': ['BAT'], 'c': ['CATTLE', 'CORN']}
    assert alphabetizer(given_list) == answer_dict


def test_spaced_string() -> None:
    """Test if the alphabetized function works correctly even if given a string with spaces inside."""
    given_list: list[str] = ["APPLE CAT", "BAT NAT", "CATTLE WE", "AIRPLANE OQ", "CO WERN"]
    answer_dict: dict[str, list[str]] = {'a': ['APPLE CAT', 'AIRPLANE OQ'], 'b': ['BAT NAT'], 'c': ['CATTLE WE', 'CO WERN']}
    assert alphabetizer(given_list) == answer_dict


def test_alphabetizer() -> None:
    """Test alphabetizer with normal arguments."""
    given_list: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    answer_dict: dict[str, list[str]] = {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
    assert alphabetizer(given_list) == answer_dict


def test_attendance_log_student() -> None:
    """Adding a student added to a already existing day."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day = "Tuesday"
    student = "Johnny"
    assert update_attendance(attendance_log, day, student) == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Johnny"]}


def test_attendance_log_day() -> None:
    """Adding a student to a new day."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day = "Wednesday"
    student = "Joseph"
    assert update_attendance(attendance_log, day, student) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa'], 'Wednesday': ['Joseph']}


def test_update_nothing() -> None:
    """Passing empty string as parameter."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(attendance_log, " ", " ") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}