class NegativeNumberError(Exception):
    pass


def check_positive(number):
    if number < 0:
        raise NegativeNumberError("The number is negative.")


# Example usage
try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)
