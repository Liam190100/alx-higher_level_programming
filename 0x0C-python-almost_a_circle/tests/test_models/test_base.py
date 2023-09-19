#!/usr/bin/python3
"""Defines unittests for base.py."""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a directory for temporary test files
        cls.test_dir = "test_files"
        os.makedirs(cls.test_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        # Clean up temporary test files
        os.rmdir(cls.test_dir)

    def setUp(self):
        # Create a sample object for testing
        self.obj = Base(1)

    def tearDown(self):
        # Remove any temporary files created during the tests
        pass

    def test_init_with_id(self):
        self.assertEqual(self.obj.id, 1)

    def test_init_without_id(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 2)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        json_str = Base.to_json_string([{"id": 1, "name": "test"}])
        self.assertEqual(json_str, '[{"id": 1, "name": "test"}]')

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string(self):
        json_str = '[{"id": 1, "name": "test"}]'
        json_list = Base.from_json_string(json_str)
        self.assertEqual(json_list, [{"id": 1, "name": "test"}])

    def test_save_to_file_empty(self):
        filename = os.path.join(self.test_dir, "empty.json")
        Base.save_to_file([], filename)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file(self):
        filename = os.path.join(self.test_dir, "data.json")
        data = [{"id": 1, "name": "test"}]
        Base.save_to_file(data)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "name": "test"}]')

    def test_update(self):
        dictionary = {"id": 1, "name": "test"}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.name, "test")

if __name__ == "__main__":
    unittest.main()

