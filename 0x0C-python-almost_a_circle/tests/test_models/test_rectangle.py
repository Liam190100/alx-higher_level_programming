#!/usr/bin/python3

"""Defines unittests for models/rectangle.py."""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
#import unittest
from models.square import square

class TestRectangle(unittest.TestCase):

    def test_init(self):
        rectangle = Rectangle(4, 5, 1, 2, 3)
        self.assertEqual(rectangle.id, 3)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)

    def test_width_property(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.width, 4)

    def test_height_property(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.height, 5)

    def test_x_property(self):
        rectangle = Rectangle(4, 5, 1)
        self.assertEqual(rectangle.x, 1)

    def test_y_property(self):
        rectangle = Rectangle(4, 5, 1, 2)
        self.assertEqual(rectangle.y, 2)

    def test_width_setter(self):
        rectangle = Rectangle(4, 5)
        rectangle.width = 6
        self.assertEqual(rectangle.width, 6)

    def test_height_setter(self):
        rectangle = Rectangle(4, 5)
        rectangle.height = 7
        self.assertEqual(rectangle.height, 7)

    def test_x_setter(self):
        rectangle = Rectangle(4, 5)
        rectangle.x = 8
        self.assertEqual(rectangle.x, 8)

    def test_y_setter(self):
        rectangle = Rectangle(4, 5)
        rectangle.y = 9
        self.assertEqual(rectangle.y, 9)

    def test_area(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_display(self):
        rectangle = Rectangle(2, 3)
        expected_output = "##\n##\n##"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_str(self):
        rectangle = Rectangle(4, 5, 1, 2, 3)
        expected_str = "[Rectangle] (3) 1/2 - 4/5"
        self.assertEqual(str(rectangle), expected_str)

    def test_update(self):
        rectangle = Rectangle(4, 5, 1, 2, 3)
        rectangle.update(6, 7, 8, 9, 10)
        self.assertEqual(rectangle.id, 6)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 9)
        self.assertEqual(rectangle.y, 10)

    def test_to_dictionary(self):
        rectangle = Rectangle(4, 5, 1, 2, 3)
        expected_dict = {'id': 3, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()

