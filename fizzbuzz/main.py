from fizzbuzz.number_marker import (DivisibleNumberMarker,
                                    ContainsNumberMarker,
                                    CrossSumDivisibleNumberMarker)

if __name__ == '__main__':
    value = ""
    divisible_number_marker = DivisibleNumberMarker(
        {3: "Fizz", 5: "Buzz", 7: "Whizz", 11: "Bang"}
    )
    contains_number_marker = ContainsNumberMarker(
        {3: "Fizz", 5: "Buzz"}
    )
    cross_divisible_number_marker = CrossSumDivisibleNumberMarker(
        {3: "Fizz", 5: "Buzz"}
    )

    input_number = 1
    while value != "FizzBuzzWhizzBangFizzBuzz":
        div_mark = divisible_number_marker.mark(input_number)
        cont_mark = contains_number_marker.mark(input_number)
        cross_mark = cross_divisible_number_marker.mark(input_number)

        value = ""
        for mark in {div_mark, cont_mark, cross_mark}:
            if mark == str(input_number):
                pass
            else:
                value += mark
        if value == "":
            value = str(input_number)

        print(value)
        input_number += 1
