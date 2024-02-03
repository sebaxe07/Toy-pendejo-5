# tests/test_utils.py

import unittest
from my_python_project.utils import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):

    def test_multiply_numbers(self):
        result = multiply_numbers(2, 3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
