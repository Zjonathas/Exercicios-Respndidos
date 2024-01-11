def decimal_to_binary(number):
    binary = ''

    while number > 0:
        binary += str(number % 2)
        number //= 2

    return binary[::-1]

print(decimal_to_binary(10))