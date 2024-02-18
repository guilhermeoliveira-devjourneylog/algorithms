import unittest
import sys
import os 
import logging
import random

# Ensure the correct path is added to sys.path for module import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.quick_sort import insertion_sort

# Set up logging
logging.basicConfig(level=logging.INFO)

class TestInsertionSort(unittest.TestCase):
    
    def setUp(self):
        """
        Set up for the test methods.
        This method is called before each test method execution.
        """
        self.arr_empty = []
        self.arr_only_one = [1]
        self.arr_only_two = [2, 1]
        self.arr_only_duplicate = [3, 2, 1, 2]
        self.arr_already_ordered = [1, 2, 3, 4, 5]
        self.arr_descending = [5, 4, 3, 2, 1]
        self.arr_negative_numbers = [3, -2, -1, 0, 2]
        self.arr_random = [random.randint(1, 1000) for _ in range(100)]

    def tearDown(self):
        """
        Tear down for the test methods.
        This method is called after each test method execution.
        """
        self.arr_empty = None
        self.arr_only_one = None
        self.arr_only_two = None
        self.arr_only_duplicate = None
        self.arr_already_ordered = None
        self.arr_descending = None
        self.arr_negative_numbers = None
        self.arr_random = None

    def test_insertion_sort_empty(self):

        self.assertEqual(insertion_sort(self.arr_empty), [], "Failed to sort an empty list")

    def test_insertion_sort_only_one(self):
  
        self.assertEqual(insertion_sort(self.arr_only_one), [1], "Failed to sort a list with a single element")

    def test_insertion_sort_only_two(self):
    
        self.assertEqual(insertion_sort(self.arr_only_two), [1, 2], "Failed to sort a list with two elements")

    def test_insertion_sort_duplicate(self):
  
        self.assertEqual(insertion_sort(self.arr_only_duplicate), [1, 2, 2, 3], "Failed to sort a list with duplicate elements")

    def test_insertion_sort_already_ordered(self):
 
        self.assertEqual(insertion_sort(self.arr_already_ordered), [1, 2, 3, 4, 5], "Failed to sort an already sorted list")

    def test_insertion_sort_descending(self):
      
        self.assertEqual(insertion_sort(self.arr_descending), [1, 2, 3, 4, 5], "Failed to sort a list in descending order")

    def test_insertion_sort_negative_numbers(self):
        
        self.assertEqual(insertion_sort(self.arr_negative_numbers), [-2, -1, 0, 2, 3], "Failed to sort a list with negative numbers")

    def test_insertion_sort_random(self):
      
        self.assertEqual(insertion_sort(self.arr_random), sorted(self.arr_random), "Failed to sort a list of random numbers")

if __name__ == '__main__':
    unittest.main()
