def fizzbuzz(number):
    reply = ""
    if number % 3 == 0:
        reply += "Fizz"

    if number % 5 == 0:
        reply += "Buzz"
    return reply if reply != "" else str(number)


if __name__ == '__main__':
    for input_number in range(100):
        print(fizzbuzz(input_number+1))

