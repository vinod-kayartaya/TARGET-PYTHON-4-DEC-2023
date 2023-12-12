import unittest
from unittest import mo
from my_utils import factorial


class FactorialTests(unittest.TestCase):

    def test_factorial_of_valid_input(self):
        expected = 120
        actual = factorial(5)
        self.assertEqual(expected, actual, f'expected is {expected} but got {actual}')
        self.assertEqual(24, factorial(4))

    def test_factorial_of_negative_input(self):
        def call_method():
            factorial(-5)
        self.assertRaises(ValueError, call_method)

    def test_factorial_of_non_numerical(self):
        def call_method():
            factorial('vinod')

        self.assertRaises(TypeError, call_method)


if __name__ == '__main__':
    unittest.main(module='ex33_unit_testing')
