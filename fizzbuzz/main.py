def fizzbuzz(number):
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return str(number)


if __name__ == '__main__':
    for input_number in range(100):
        print(fizzbuzz(input_number+1))

