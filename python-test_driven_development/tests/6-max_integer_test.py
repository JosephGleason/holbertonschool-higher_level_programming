#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer function."""

    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_args(self):
        """Test that calling max_integer() with no args returns None."""
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_sorted_list(self):
        """Test a sorted list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_duplicates(self):
        """Test list where all elements are the same."""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_negative_numbers(self):
        """Test list with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_ints(self):
        """Test list mixing negative, zero, and positive ints."""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_floats(self):
        """Test list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_ints_floats(self):
        """Test list mixing ints and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_large_list(self):
        """Test with a large list of increasing numbers."""
        self.assertEqual(max_integer(list(range(1000))), 999)


if __name__ == '__main__':
    unittest.main()
