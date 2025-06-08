#!/usr/bin/python3
"""Defines a function that appends a string to a file"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8)
    and returns the number of characters added:
    Args:
        filename (str): name of the file to append to
        text (str): string to append to the file
    Returns:
        int: the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
