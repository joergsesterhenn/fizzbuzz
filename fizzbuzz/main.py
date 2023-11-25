import string

numbers_to_mark = {3: "Fizz", 5: "Buzz"}


def fizzbuzz(number) -> string:
    marker_for_dividability = ""
    marker_for_being_part_of = ""
    marker = ""
    for divisor in numbers_to_mark:
        marker_for_dividability += (
            append_marker_for_dividability(number, divisor))
    for part in numbers_to_mark:
        marker_for_being_part_of += (
            append_marker_for_being_part_of(number, part))
        marker = marker_for_being_part_of + marker_for_dividability
    return marker if marker != "" else str(number)


def append_marker_for_dividability(number, divisor) -> string:
    if dividable_by(number, divisor):
        return numbers_to_mark[divisor]
    else:
        return ""


def append_marker_for_being_part_of(number, part) -> string:
    if is_part_of(number, part):
        return numbers_to_mark[part]
    else:
        return ""


def is_part_of(number, character) -> bool:
    return str(number).find(str(character)) != -1


def dividable_by(number, divisor) -> bool:
    return number % divisor == 0


if __name__ == '__main__':
    for input_number in range(100):
        print(fizzbuzz(input_number+1))
