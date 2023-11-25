import unittest
from fizzbuzz import main


class FizzBuzzTestCase(unittest.TestCase):
    def test_returns_number_for_1(self):
        reply = main.fizzbuzz(1)
        self.assertEqual("1", reply)

    def test_returns_number_for_2(self):
        reply = main.fizzbuzz(2)
        self.assertEqual("2", reply)

    def test_returns_fizz_for_3(self):
        reply = main.fizzbuzz(3)
        self.assertEqual("Fizz", reply)

    def test_returns_number_for_4(self):
        reply = main.fizzbuzz(4)
        self.assertEqual("4", reply)

    def test_returns_buzz_for_5(self):
        reply = main.fizzbuzz(5)
        self.assertEqual("Buzz", reply)

    def test_returns_fizz_for_6(self):
        reply = main.fizzbuzz(6)
        self.assertEqual("Fizz", reply)

    def test_returns_number_for_7(self):
        reply = main.fizzbuzz(7)
        self.assertEqual("7", reply)

    def test_returns_number_for_8(self):
        reply = main.fizzbuzz(8)
        self.assertEqual("8", reply)

    def test_returns_fizz_for_9(self):
        reply = main.fizzbuzz(9)
        self.assertEqual("Fizz", reply)

    def test_returns_buzz_for_10(self):
        reply = main.fizzbuzz(10)
        self.assertEqual("Buzz", reply)


if __name__ == '__main__':
    unittest.main()
