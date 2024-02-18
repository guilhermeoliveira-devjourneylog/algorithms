import unittest
import sys
import os 
import logging

# Ensure the correct path is added to sys.path for module import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.quick_sort import quicksort, partition

# Set up logging
logging.basicConfig(level=logging.INFO)

class QuickSort(unittest.TestCase):
    
    def test_quicksort(self):
        arr = [5, 3, 1, 2, 6, 4]
        quicksort(arr, 0, len(arr), 0, partition)
        print(f"Unit Testing Return from test_quicksort: {arr}")
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6])

    def test_quicksort_empty(self):
        arr = []
        quicksort(arr, 0, len(arr), 0, partition)
        print(f"Unit Testing Return from test_quicksort_empty: {arr}")
        self.assertEqual(arr, [])

    def test_quicksort_one_element(self):
        arr = [1]
        quicksort(arr, 0, len(arr), 0, partition)
        print(f"Unit Testing Return from test_quicksort_one_element: {arr}")
        self.assertEqual(arr, [1])

if __name__ == '__main__':
    unittest.main()