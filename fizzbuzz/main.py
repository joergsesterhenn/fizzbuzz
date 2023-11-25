numbers_to_mark = {3: "Fizz", 5: "Buzz"}


def fizzbuzz(number):
    marker_for_divisibility = ""
    for divisor in numbers_to_mark:
        marker_for_divisibility += append_marker(number, divisor)
    return marker_for_divisibility \
        if marker_for_divisibility != "" \
        else str(number)


def append_marker(number, divisor):
    if dividable_by(number, divisor):
        return numbers_to_mark[divisor]
    else:
        return ""


def dividable_by(number, divisor):
    return number % divisor == 0


if __name__ == '__main__':
    for input_number in range(100):
        print(fizzbuzz(input_number+1))
