#!/usr/bin/env python3
""" unittests for utils functions
"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ test access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test that the method returns what its supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
