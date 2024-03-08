#!/usr/bin/python3
"""State Class Unit Tests Module"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State

import unittest

class TestState(unittest.TestCase):
  """TestState Class"""

  def setUp(self):
    """Method to setup test cases"""

    pass

  def tearDown(self):
    """Method to tear down the current environment"""
    
    pass

  def test_init(self):
    """Method to test no kwargs init of the class"""

    obj = State()
    self.assertIsInstance(obj, State)
    self.assertTrue(issubclass(type(obj), BaseModel))
    self.assertIsInstance(obj.id, str)
    self.assertIsInstance(obj.created_at, datetime)
    self.assertIsInstance(obj.updated_at, datetime)
    self.assertEqual(obj.name, "")

  def test_init_kwargs(self):
    """Method to test init with kwargs"""

    created_at = "2023-01-01T12:00:00.000001"
    updated_at = "2023-01-01T12:30:00.000002"
    name = "Stuff"
    obj = State(created_at=created_at, updated_at=updated_at, name=name)

    self.assertEqual(obj.created_at.isoformat(), created_at)
    self.assertEqual(obj.updated_at.isoformat(), updated_at)
    self.assertEqual(obj.name, name)

  def test_to_dict(self):
    """Method to test the to_dict functionality"""
    
    obj = State()
    State_dict = obj.to_dict()
    keys = ['id', 'created_at', 'updated_at', 'name', '__class__']

    for key in keys:
        self.assertIn(key, State_dict)

  if __name__ == "__main__":
    unittest.main()