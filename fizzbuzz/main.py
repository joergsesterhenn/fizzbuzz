import string

numbers_to_mark = {3: "Fizz", 5: "Buzz", 7: "Whizz", 11: "Bang"}


def fizzbuzz(number) -> string:
    marker = ""
    for divisor in numbers_to_mark:
        marker += (
            append_marker_for_divisibility(number, divisor))
    return marker if marker != "" else str(number)


def append_marker_for_divisibility(number, divisor) -> string:
    if divisible_by(number, divisor):
        return numbers_to_mark[divisor]
    else:
        return ""


def divisible_by(number, divisor) -> bool:
    return number % divisor == 0


if __name__ == '__main__':
    value = ""
    input_number = 1
    while value != "FizzBuzzWhizzBang":
        value = fizzbuzz(input_number)
        print(value)
        input_number += 1
