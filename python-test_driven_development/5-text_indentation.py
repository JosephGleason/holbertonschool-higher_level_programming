#!/usr/bin/python3
"""
This module prints a text with 2 new lines after ., ? and :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after ., ? and :.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    start = 0
    length = len(text)
    for i, c in enumerate(text):
        if c in ".:?":
            print(text[start:i + 1].strip())
            # Solo imprime salto si no es el último carácter
            if i + 1 < length:
                print()
            start = i + 1
    if start < length:
        print(text[start:].strip())
