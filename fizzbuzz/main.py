from fizzbuzz.number_marker import DivisibleNumberMarker, ContainsNumberMarker

if __name__ == '__main__':
    value = ""
    divisible_number_marker = DivisibleNumberMarker(
        {3: "Fizz", 5: "Buzz", 7: "Whizz", 11: "Bang"}
    )
    contains_number_marker = ContainsNumberMarker(
        {3: "Fizz", 5: "Buzz"}
    )
    input_number = 1
    while value != "FizzBuzzWhizzBangFizzBuzz":
        div_mark = divisible_number_marker.mark(input_number)
        cont_mark = contains_number_marker.mark(input_number)
        if div_mark == str(input_number):
            value = cont_mark
        elif cont_mark == str(input_number):
            value = div_mark
        else:
            value = div_mark + cont_mark
        print(value)
        # print(input_number)
        input_number += 1
