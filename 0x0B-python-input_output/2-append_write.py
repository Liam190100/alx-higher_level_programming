#!/usr/bin/python3
"""
Fuction that write in the file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and
    returns the number of characters written.

    :param filename: (str) The name of the file
    write to (default is an empty string).
    :param text: (str) The text
    write to the file (default is an empty string).
    :return: (int) The number of characters successfully
    written to the file, or 0 on failure.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            char_count = file.write(text)
        return char_count
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0  # Return 0 to indicate failure.
