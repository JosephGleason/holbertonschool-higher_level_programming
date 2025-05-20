#!/usr/bin/python3
"""
5-text_indentation.py
Module: provides a function to prt indented text with 2 \n after ., ?, and :
"""


def text_indentation(text):
    """Prints a text with 2 lines after each of these character ".?:"

    Args:
        text (str): must be a string

    Raises:
        TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    notebook = ''
    length = len(text)
    for idx, char in enumerate(text):
        notebook += char
        if char in ".?:":
            print(notebook.strip())
            # Only one blank line between segments (two newlines total)
            if idx != length - 1:
                print()
            notebook = ""
        # after the loop, print any remaining text
    if notebook:
        print(notebook.strip())
