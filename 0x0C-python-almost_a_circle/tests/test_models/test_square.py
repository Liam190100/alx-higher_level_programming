#!/usr/bin/python3

"""Defines unittests for models/square.py."""

#import io
#import sys
#import unittest
#from models.base import Base
#from models.square import Square

    """Unittests for testing instantiation of the Square class."""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_str(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_size_property(self):
        square = Square(4)
        self.assertEqual(square.size, 4)

    def test_size_setter(self):
        square = Square(3)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_update_args(self):
        square = Square(2, 1, 1, 1)
        square.update(2, 3, 3, 4)
        self.assertEqual(str(square), "[Square] (2) 3/3 - 4")

    def test_update_kwargs(self):
        square = Square(2, 1, 1, 1)
        square.update(id=2, size=3, x=3, y=4)
        self.assertEqual(str(square), "[Square] (2) 3/4 - 3")

    def test_to_dictionary(self):
        square = Square(3, 2, 2, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 3, 'x': 2, 'y': 2}
        self.assertEqual(square_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
