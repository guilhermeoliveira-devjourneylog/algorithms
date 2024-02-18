import unittest
import sys
import os 
import logging

# Adds the correct path to sys.path for module import.
# This is necessary because the module we are testing is in a different directory.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports the functions from the KargerMinCut module that will be tested.
from algorithms.karger_min_cut import contract_vertices, perform_randomized_contraction, read_graph, find_minimum_cut

# Sets up logging to display information about the log level.
logging.basicConfig(level=logging.INFO)

class TestKargerMinCut(unittest.TestCase):
    """
    Test class for the KargerMinCut module.
    This class inherits from unittest.TestCase, which is the base class for all tests in the unittest module.
    """
   
    def setUp(self):
        """
        Setup for the test methods.
        This method is called before each test method execution.
        Here, we are setting up a test graph that will be used in each test.
        """ 
        self.graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}

    def tearDown(self):
        """
        Teardown for the test methods.
        This method is called after each test method execution.
        Here, we are clearing the test graph to ensure there are no side effects between tests.
        """
        self.graph = None

    def test_contract_vertices(self):
        """
        Tests the contract_vertices function.
        This function should contract two vertices into one and remove self-loop edges.
        We check if the function is working correctly by comparing the result with the expected one.
        """
        contract_vertices(self.graph, 1, 2)
        self.assertEqual(self.graph, {1: [3, 3], 3: [1, 1]})

    def test_perform_randomized_contraction(self):
        """
        Tests the perform_randomized_contraction function.
        This function should perform the randomized contraction algorithm until only two vertices remain.
        We check if the function is working correctly by comparing the result with the expected one.
        """
        result = perform_randomized_contraction(self.graph)
        self.assertEqual(result, 2)

    def test_read_graph(self):
        """
        Tests the read_graph function.
        This function should read a graph from a file.
        We check if the function is working correctly by comparing the result with the expected one.
        """
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\test-graph-karger-min-cut.txt'
        self.graph = read_graph(file_path)
        self.assertEqual(self.graph, {1: [2, 3], 2: [1, 3], 3: [1, 2]})

    def test_find_minimum_cut(self):
        """
        Tests the find_minimum_cut function.
        This function should find the minimum cut of a graph using the randomized contraction algorithm.
        We check if the function is working correctly by comparing the result with the expected one.
        """
        min_cut = find_minimum_cut(self.graph)
        self.assertEqual(min_cut, 2)

if __name__ == '__main__':
    unittest.main()
