import unittest
import sys
import os 

# Ensure the correct path is added to sys.path for module import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from QuickSort import read_file

class TestFileMethods(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "test_file.txt"
        with open(self.test_file, "w") as file:
            file.write("1\n2\n3\n4\n5")

    def test_read_file(self):
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(read_file(self.test_file), expected_output)

    def tearDown(self):
        os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()
