#!/usr/bin/env python3
""" unittests for utils functions
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch


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

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """  test that a KeyError is raised for the given inputs
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ test that utils.get_json returns the expected result
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_request):
        """ test that the output of get_json is equal to test_payload
        """
        mock_request.json.return_value = test_payload
        mock_request.return_value = mock_request
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''This class tests memoization'''
    def test_memoize(self):
        '''Test the memoize and compare results'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as test_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, test_method.return_value)
            self.assertEqual(test_class.a_property, test_method.return_value)
            test_method.assert_called_once()
