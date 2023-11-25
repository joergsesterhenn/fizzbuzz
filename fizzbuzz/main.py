def fizzbuzz(number):
    if number==5:
        return "Buzz"
    return "Fizz"


if __name__ == '__main__':
    for input_number in range(100):
        print(fizzbuzz(input_number+1))

