from fizzbuzz.number_marker import DivisibleNumberMarker

if __name__ == '__main__':
    value = ""
    number_marker = DivisibleNumberMarker(
        {3: "Fizz", 5: "Buzz", 7: "Whizz", 11: "Bang"}
    )
    input_number = 1
    while value != "FizzBuzzWhizzBang":
        value = number_marker.mark(input_number)
        print(value)
        input_number += 1
