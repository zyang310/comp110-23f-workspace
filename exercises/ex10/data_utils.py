"""Dictionary related utility functions."""
from csv import DictReader
__author__ = "730713735"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read cvs file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Return a list of all values under a specific header."""
    results: list[str] = []
    # loop through each element of the list
    for elem in table:
        # for each dictionary, get the value at key "header" and add that to result
        results.append(elem[key])
    return results


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Return a list of all values under a specific header."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for elem in first_row:
        result[elem] = column_values(table, elem)
    return result


def head(col_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns a column-based table with the first n rows of data for each column."""
    dictionary: dict[str, list[str]] = {}
    if rows >= len(col_table):
        return col_table
    for i in col_table:
        a_list: list[str] = []
        counter: int = 0
        while counter < rows:
            a_list.append(col_table[i][counter])
            counter += 1
        dictionary[i] = a_list
    return dictionary


def select(col_table: dict[str, list[str]], col_name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    dictionary: dict[str, list[str]] = {}
    for elem in col_name:
        dictionary[elem] = col_table[elem]
    return dictionary


def concat(first_column: dict[str, list[str]], second_column: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two cloumn-based tables combined."""
    dictionary: dict[str, list[str]] = {}
    for elem in first_column:
        dictionary[elem] = first_column[elem]
    for i in second_column:
        if i in dictionary:
            for x in second_column[i]:
                dictionary[i].append(x)
        else:
            dictionary[i] = second_column[i]
    return dictionary


def count(value_list: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the cound of the numbre of times that value appeared in the input list."""
    dictionary: dict[str, int] = {}
    for item in value_list:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary