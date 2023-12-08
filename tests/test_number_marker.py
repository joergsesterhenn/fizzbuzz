import unittest

from fizzbuzz.number_marker import (DivisibleNumberMarker,
                                    ContainsNumberMarker,
                                    CrossSumDivisibleNumberMarker)

divisible_number_marker = DivisibleNumberMarker(
    {3: "Fizz", 5: "Buzz", 7: "Whizz", 11: "Bang"}
)

cross_sum_divisible_number_marker = CrossSumDivisibleNumberMarker(
    {3: "Fizz", 5: "Buzz"}
)

contains_number_marker = ContainsNumberMarker(
    {3: "Fizz", 5: "Buzz"}
)


class DivisibleNumberMarkerTestCase(unittest.TestCase):
    def test_returns_nothing_for_1(self):
        reply = divisible_number_marker.mark(1)
        self.assertEqual("", reply)

    def test_returns_nothing_for_2(self):
        reply = divisible_number_marker.mark(2)
        self.assertEqual("", reply)

    def test_returns_fizz_for_3(self):
        reply = divisible_number_marker.mark(3)
        self.assertEqual("Fizz", reply)

    def test_returns_nothing_for_4(self):
        reply = divisible_number_marker.mark(4)
        self.assertEqual("", reply)

    def test_returns_buzz_for_5(self):
        reply = divisible_number_marker.mark(5)
        self.assertEqual("Buzz", reply)

    def test_returns_fizz_for_6(self):
        reply = divisible_number_marker.mark(6)
        self.assertEqual("Fizz", reply)

    def test_returns_whizz_for_7(self):
        reply = divisible_number_marker.mark(7)
        self.assertEqual("Whizz", reply)

    def test_returns_nothing_for_8(self):
        reply = divisible_number_marker.mark(8)
        self.assertEqual("", reply)

    def test_returns_fizz_for_9(self):
        reply = divisible_number_marker.mark(9)
        self.assertEqual("Fizz", reply)

    def test_returns_buzz_for_10(self):
        reply = divisible_number_marker.mark(10)
        self.assertEqual("Buzz", reply)

    def test_returns_fizzbuzz_for_15(self):
        reply = divisible_number_marker.mark(15)
        self.assertEqual("FizzBuzz", reply)


class CrossSumDivisibleNumberMarkerTestCase(unittest.TestCase):
    def test_returns_nothing_for_1(self):
        reply = cross_sum_divisible_number_marker.mark(1)
        self.assertEqual("", reply)

    def test_returns_nothing_for_2(self):
        reply = cross_sum_divisible_number_marker.mark(2)
        self.assertEqual("", reply)

    def test_returns_fizz_for_3(self):
        reply = cross_sum_divisible_number_marker.mark(3)
        self.assertEqual("Fizz", reply)

    def test_returns_nothing_for_4(self):
        reply = cross_sum_divisible_number_marker.mark(4)
        self.assertEqual("", reply)

    def test_returns_buzz_for_5(self):
        reply = cross_sum_divisible_number_marker.mark(5)
        self.assertEqual("Buzz", reply)

    def test_returns_fizz_for_6(self):
        reply = cross_sum_divisible_number_marker.mark(6)
        self.assertEqual("Fizz", reply)

    def test_returns_numebr_for_7(self):
        reply = cross_sum_divisible_number_marker.mark(7)
        self.assertEqual("", reply)

    def test_returns_nothing_for_8(self):
        reply = cross_sum_divisible_number_marker.mark(8)
        self.assertEqual("", reply)

    def test_returns_fizz_for_9(self):
        reply = cross_sum_divisible_number_marker.mark(9)
        self.assertEqual("Fizz", reply)

    def test_returns_nothing_for_10(self):
        reply = cross_sum_divisible_number_marker.mark(10)
        self.assertEqual("", reply)

    def test_returns_fizz_for_12(self):
        reply = cross_sum_divisible_number_marker.mark(12)
        self.assertEqual("Fizz", reply)

    def test_returns_fizz_for_15(self):
        reply = cross_sum_divisible_number_marker.mark(15)
        self.assertEqual("Fizz", reply)

    def test_returns_buzz_for_23(self):
        reply = cross_sum_divisible_number_marker.mark(23)
        self.assertEqual("Buzz", reply)


class ContainsNumberMarkerTestCase(unittest.TestCase):
    def test_returns_nothing_for_1(self):
        reply = contains_number_marker.mark(1)
        self.assertEqual("", reply)

    def test_returns_nothing_for_2(self):
        reply = contains_number_marker.mark(2)
        self.assertEqual("", reply)

    def test_returns_fizz_for_3(self):
        reply = contains_number_marker.mark(3)
        self.assertEqual("Fizz", reply)

    def test_returns_nothing_for_4(self):
        reply = contains_number_marker.mark(4)
        self.assertEqual("", reply)

    def test_returns_buzz_for_5(self):
        reply = contains_number_marker.mark(5)
        self.assertEqual("Buzz", reply)

    def test_returns_nothing_for_6(self):
        reply = contains_number_marker.mark(6)
        self.assertEqual("", reply)

    def test_returns_nothing_for_7(self):
        reply = contains_number_marker.mark(7)
        self.assertEqual("", reply)

    def test_returns_nothing_for_8(self):
        reply = contains_number_marker.mark(8)
        self.assertEqual("", reply)

    def test_returns_nothing_for_9(self):
        reply = contains_number_marker.mark(9)
        self.assertEqual("", reply)

    def test_returns_nothing_for_10(self):
        reply = contains_number_marker.mark(10)
        self.assertEqual("", reply)

    def test_returns_buzz_for_15(self):
        reply = contains_number_marker.mark(15)
        self.assertEqual("Buzz", reply)


if __name__ == '__main__':
    unittest.main()
