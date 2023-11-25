import unittest
from fizzbuzz import main

class FizzBuzzTestCase(unittest.TestCase):
    def test_returns_fizz_for_3(self):
        reply = main.fizzbuzz(3)
        self.assertEqual("Fizz", reply)


if __name__ == '__main__':
    unittest.main()
