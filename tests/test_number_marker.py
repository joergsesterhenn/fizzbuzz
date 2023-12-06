import unittest

from fizzbuzz.number_marker import DivisibleNumberMarker, ContainsNumberMarker

divisible_number_marker = DivisibleNumberMarker(
    {3: "Fizz", 5: "Buzz", 7: "Whizz", 11: "Bang"}
)

contains_number_marker = ContainsNumberMarker(
    {3: "Fizz", 5: "Buzz"}
)


class DivisibleNumberMarkerTestCase(unittest.TestCase):
    def test_returns_number_for_1(self):
        reply = divisible_number_marker.mark(1)
        self.assertEqual("1", reply)

    def test_returns_number_for_2(self):
        reply = divisible_number_marker.mark(2)
        self.assertEqual("2", reply)

    def test_returns_fizz_for_3(self):
        reply = divisible_number_marker.mark(3)
        self.assertEqual("Fizz", reply)

    def test_returns_number_for_4(self):
        reply = divisible_number_marker.mark(4)
        self.assertEqual("4", reply)

    def test_returns_buzz_for_5(self):
        reply = divisible_number_marker.mark(5)
        self.assertEqual("Buzz", reply)

    def test_returns_fizz_for_6(self):
        reply = divisible_number_marker.mark(6)
        self.assertEqual("Fizz", reply)

    def test_returns_whizz_for_7(self):
        reply = divisible_number_marker.mark(7)
        self.assertEqual("Whizz", reply)

    def test_returns_number_for_8(self):
        reply = divisible_number_marker.mark(8)
        self.assertEqual("8", reply)

    def test_returns_fizz_for_9(self):
        reply = divisible_number_marker.mark(9)
        self.assertEqual("Fizz", reply)

    def test_returns_buzz_for_10(self):
        reply = divisible_number_marker.mark(10)
        self.assertEqual("Buzz", reply)

    def test_returns_fizzbuzz_for_15(self):
        reply = divisible_number_marker.mark(15)
        self.assertEqual("FizzBuzz", reply)


class ContainsNumberMarkerTestCase(unittest.TestCase):
    def test_returns_number_for_1(self):
        reply = contains_number_marker.mark(1)
        self.assertEqual("1", reply)

    def test_returns_number_for_2(self):
        reply = contains_number_marker.mark(2)
        self.assertEqual("2", reply)

    def test_returns_fizz_for_3(self):
        reply = contains_number_marker.mark(3)
        self.assertEqual("Fizz", reply)

    def test_returns_number_for_4(self):
        reply = contains_number_marker.mark(4)
        self.assertEqual("4", reply)

    def test_returns_buzz_for_5(self):
        reply = contains_number_marker.mark(5)
        self.assertEqual("Buzz", reply)

    def test_returns_number_for_6(self):
        reply = contains_number_marker.mark(6)
        self.assertEqual("6", reply)

    def test_returns_number_for_7(self):
        reply = contains_number_marker.mark(7)
        self.assertEqual("7", reply)

    def test_returns_number_for_8(self):
        reply = contains_number_marker.mark(8)
        self.assertEqual("8", reply)

    def test_returns_number_for_9(self):
        reply = contains_number_marker.mark(9)
        self.assertEqual("9", reply)

    def test_returns_number_for_10(self):
        reply = contains_number_marker.mark(10)
        self.assertEqual("10", reply)

    def test_returns_buzz_for_15(self):
        reply = contains_number_marker.mark(15)
        self.assertEqual("Buzz", reply)


if __name__ == '__main__':
    unittest.main()
