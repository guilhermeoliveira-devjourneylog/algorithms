import unittest
import sys
import os 
import logging

# Ensure the correct path is added to sys.path for module import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.quick_sort import partition, partition_median, partition_last

# Set up logging
logging.basicConfig(level=logging.INFO)

class TestPartitionMethods(unittest.TestCase):
   
    def setUp(self):
        """
        Set up for the test methods.
        This method is called before each test method execution.
        """
        self.arr_partition = [5, 3, 1, 2, 6, 4]
        self.partition_sorted = [1, 2, 3, 4, 5, 6]
        self.partition_reverse_sorted = [6, 5, 4, 3, 2, 1]
        self.partition_duplicates = [5, 3, 1, 2, 5, 4]
        self.partition_negative_case = [5, 3, 1, 2, 6, 4]
        self.partition_median_positive_case = [5, 3, 1, 2, 6, 4]
        self.partition_median_sorted = [1, 2, 3, 4, 5, 6]
        self.partition_median_reverse_sorted = [6, 5, 4, 3, 2, 1]
        self.partition_median_duplicates = [5, 3, 1, 2, 5, 4]
        self.partition_median_negative_case = [5, 3, 1, 2, 6, 4]
        self.partition_last = [5, 3, 1, 2, 6, 4]

    def tearDown(self):
        """
        Tear down for the test methods.
        This method is called after each test method execution.
        """
        self.arr_partition = None
        self.partition_sorted = None
        self.partition_reverse_sorted = None
        self.partition_duplicates = None
        self.partition_negative_case = None
        self.partition_median_positive_case = None
        self.partition_median_sorted = None
        self.partition_median_reverse_sorted = None
        self.partition_median_duplicates = None
        self.partition_median_negative_case = None
        self.partition_last = None

    def test_partition_positive_case(self):
        """
        Test case for the partition method with a positive scenario.
        This test case checks if the partition method correctly partitions an unsorted array.
        The expected output is a partitioned array and the pivot index.
        """ 
        pivot_index = partition(self.arr_partition, 0, len(self.arr_partition)-1)
        print(f"Unit Testing Array after partition: {self.arr_partition}")
        print(f"Unit Testing Return from test_partition pivot: {pivot_index}")
        self.assertEqual(self.arr_partition, [2, 3, 1, 5, 6, 4])
        self.assertEqual(pivot_index, 3)
        
    def test_partition_sorted(self):
        """
        Test case for the partition method with a sorted array.
        This test case checks if the partition method correctly partitions a sorted array.
        The expected output is the same sorted array and the pivot index as 0.
        """ 
        pivot_index = partition(self.partition_sorted, 0, len(self.partition_sorted)-1)
        print(f"Unit Testing Array partition_sorted: {self.partition_sorted}")
        print(f"Unit Testing Return from partition_sorted pivot: {pivot_index}")
        self.assertEqual(self.partition_sorted, [1, 2, 3, 4, 5, 6])
        self.assertEqual(pivot_index, 0)

    def test_partition_reverse_sorted(self):
        """
        Test case for the partition method with a reverse sorted array.
        This test case checks if the partition method correctly partitions a reverse sorted array.
        The expected output is a partitioned array and the pivot index.
        """ 
        pivot_index = partition(self.partition_reverse_sorted, 0, len(self.partition_reverse_sorted)-1)
        print(f"Unit Testing Array partition_reverse_sorted: {self.partition_reverse_sorted}")
        print(f"Unit Testing Return from partition_reverse_sorted pivot: {pivot_index}")
        self.assertEqual(self.partition_reverse_sorted, [2, 5, 4, 3, 6, 1])
        self.assertEqual(pivot_index, 4)

    def test_partition_duplicates(self):
        """
        Test case for the partition method with an array that contains duplicate elements.
        This test case checks if the partition method correctly partitions an array with duplicate elements.
        The expected output is a partitioned array and the pivot index.
        """ 
        pivot_index = partition(self.partition_duplicates, 0, len(self.partition_duplicates)-1)
        print(f"Unit Testing Array partition_duplicates: {self.partition_duplicates}")
        print(f"Unit Testing Return from partition_duplicates pivot: {pivot_index}")
        self.assertEqual(self.partition_duplicates, [2, 3, 1, 5, 5, 4])
        self.assertEqual(pivot_index, 3)
        
    def test_partition_negative_case(self):
        """
        Test case for the partition method with a negative scenario.
        This test case checks if the partition method correctly handles a negative scenario.
        The expected output is a partitioned array and the pivot index, which should not be the same as the input.
        """ 
        pivot_index = partition(self.partition_negative_case, 0, len(self.partition_negative_case)-1)
        print(f"Unit Testing Array after partition_negative: {self.partition_negative_case}")
        print(f"Unit Testing Return from partition_negative pivot: {pivot_index}")
        self.assertNotEqual(self.partition_negative_case, [5, 3, 1, 2, 6, 4])
        self.assertNotEqual(pivot_index, 0)

    def test_partition_median_positive_case(self):
        """
        Test case for the partition_median method with a positive scenario.
        This test case checks if the partition_median method correctly partitions an unsorted array.
        The expected output is a partitioned array and the pivot index.
        """ 
        pivot_index = partition_median(self.partition_median_positive_case, 0, len(self.partition_median_positive_case)-1)
        print(f"Unit Testing Array after partition_median: {self.partition_median_positive_case}")
        print(f"Unit Testing Return from test_partition_median pivot: {pivot_index}")
        self.assertEqual(self.partition_median_positive_case, [2, 3, 1, 5, 6, 4])
        self.assertEqual(pivot_index, 3)

    def test_partition_median_sorted(self):
        """
        Test case for the partition median method with a sorted array.
        This test case checks if the partition_median method correctly partitions a sorted array.
        The expected output is the same sorted array and the pivot index as the median index.
        """ 
        pivot_index = partition_median(self.partition_median_sorted, 0, len(self.partition_median_sorted)-1)
        print(f"Unit Testing Array partition_sorted: {self.partition_median_sorted}")
        print(f"Unit Testing Return from partition_sorted pivot: {pivot_index}")
        self.assertEqual(self.partition_median_sorted, [1, 2, 3, 4, 5, 6])
        self.assertEqual(pivot_index, 2)

    def test_partition_median_reverse_sorted(self):
        """
        Test case for the partition median method with a reverse sorted array.
        This test case checks if the partition_median method correctly partitions a reverse sorted array.
        The expected output is a partitioned array and the pivot index as the median index.
        """ 
        pivot_index = partition_median(self.partition_median_reverse_sorted, 0, len(self.partition_median_reverse_sorted)-1)
        print(f"Unit Testing Array partition_reverse_sorted: {self.partition_median_reverse_sorted}")
        print(f"Unit Testing Return from partition_reverse_sorted pivot: {pivot_index}")
        self.assertEqual(self.partition_median_reverse_sorted, [2, 3, 4, 5, 6, 1])
        self.assertEqual(pivot_index, 2)

    def test_partition_median_duplicates(self):
        """
        Test case for the partition median method with an array that contains duplicate elements.
        This test case checks if the partition_median method correctly partitions an array with duplicate elements.
        The expected output is a partitioned array and the pivot index.
        """ 
        pivot_index = partition_median(self.partition_median_duplicates, 0, len(self.partition_median_duplicates)-1)
        print(f"Unit Testing Array partition_duplicates: {self.partition_median_duplicates}")
        print(f"Unit Testing Return from partition_duplicates pivot: {pivot_index}")
        self.assertEqual(self.partition_median_duplicates, [2, 3, 1, 5, 5, 4])
        self.assertEqual(pivot_index, 3)
        
    def test_partition_median_negative_case(self):
        """
        Test case for the partition_median method with a negative scenario.
        This test case checks if the partition_median method correctly handles a negative scenario.
        The expected output is a partitioned array and the pivot index, which should not be the same as the input.
        """ 
        pivot_index = partition_median(self.partition_median_negative_case, 0, len(self.partition_median_negative_case)-1)
        print(f"Unit Testing Array after partition_median_negative: {self.partition_median_negative_case}")
        print(f"Unit Testing Return from partition_median_negative pivot: {pivot_index}")
        self.assertNotEqual(self.partition_median_negative_case, [5, 3, 1, 2, 6, 4])
        self.assertNotEqual(pivot_index, 0)
        
    def test_partition_last(self):
        """
        Test case for the partition_last method.
        This test case checks if the partition_last method correctly partitions an array.
        The expected output is the same input array and the pivot index as the last index.
        """ 
        pivot_index = partition_last(self.partition_last, 0, len(self.partition_last)-1)
        print(f"Unit Testing Array after partition_last: {self.partition_last}")
        print(f"Unit Testing Return from test_partition_last pivot: {pivot_index}")
        self.assertEqual(self.partition_last, [5, 3, 1, 2, 6, 4])
        self.assertEqual(pivot_index, 4)

if __name__ == '__main__':
    unittest.main()
