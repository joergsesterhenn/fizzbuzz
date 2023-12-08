from fizzbuzz.list_printer import MarkedNumberListPrinter
from fizzbuzz.number_marker import (DivisibleNumberMarker,
                                    ContainsNumberMarker,
                                    CrossSumDivisibleNumberMarker)

if __name__ == '__main__':

    number_markers = [
        DivisibleNumberMarker({3: "Fizz", 5: "Buzz", 7: "Whizz", 11: "Bang"}),
        ContainsNumberMarker({3: "Fizz", 5: "Buzz"}),
        CrossSumDivisibleNumberMarker({3: "Fizz", 5: "Buzz"})
    ]

    list_printer = MarkedNumberListPrinter(number_markers)
    list_printer.print(1, "FizzBuzzWhizzBangFizzBuzz")
