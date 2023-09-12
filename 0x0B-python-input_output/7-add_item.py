#!/usr/bin/python3
import sys
import json

def save_to_json_file(my_obj, filename):
    """
    Save the provided Python object as JSON data in the specified file.

    :param my_obj: The Python object to be saved as JSON.
    :param filename: The name of the file to save the JSON data.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """
    Load JSON data from the specified file and return it as a Python object.

    :param filename: The name of the file containing JSON data.
    :return: The Python object loaded from the JSON data.
    """
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    try:
        # Load the existing data from 'add_item.json' if it exists, or initialize an empty list.
        try:
            data = load_from_json_file('add_item.json')
        except FileNotFoundError:
            data = []

        # Add command-line arguments to the list.
        data.extend(sys.argv[1:])

        # Save the updated list back to 'add_item.json'.
        save_to_json_file(data, 'add_item.json')

        print("Arguments added and saved successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
