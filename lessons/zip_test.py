"""Testing CO5 Zip assignment."""

__author__ = "730713735"

from lessons.zip import zip


def test_empty_list() -> None:
    """Test two empty list arugments."""
    str_empty_list: list[str] = []
    int_empty_list: list[int] = []
    assert zip(str_empty_list, int_empty_list) == {}


def test_zip_positives() -> None:
    """Test two list with positive integers."""
    answer = {'Happy': 1, 'Tuesday': 2}
    str_list: list[str] = ["Happy", "Tuesday"]
    int_list: list[int] = [1, 2]
    assert zip(str_list, int_list) == answer


def test_zip_negatives() -> None:
    """Test two list with negative value integers."""
    answer = {'Happy': -1, 'Tuesday': -3}
    str_list: list[str] = ["Happy", "Tuesday"]
    int_list: list[int] = [-1, -3]
    assert zip(str_list, int_list) == answer


def test_zip_different_length_list() -> None:
    """Test two list with different length."""
    str_list: list[str] = ["cat", "dog", "bird", "turte"]
    int_list: list[int] = [3, 5]
    assert zip(str_list, int_list) == {}