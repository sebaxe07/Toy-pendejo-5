# tests/test_main.py

import unittest
from my_python_project.main import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
