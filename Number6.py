def divide_numbers(numerator, denominator):
    """
    Divides two numbers and handles exceptions.

    Parameters:
    numerator (int or float): The numerator.
    denominator (int or float): The denominator.

    Returns:
    float: The result of the division if successful.
    None: If an error occurs.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers only.")

# Example usage
print(divide_numbers(100, 20))   # Output: 5.0
print(divide_numbers(5, 0))   # Output: Error message
print(divide_numbers(100, "a")) # Output: Error message

