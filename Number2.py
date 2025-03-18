def classify_number(n):
    """
    Classifies a number as Positive, Negative, or Zero.

    Parameters:
    n (int): The integer to classify.

    Returns:
    str: "Positive" if n > 0, "Negative" if n < 0, or "Zero" if n == 0.
    """
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"


def calculate_average(*args):
    """
    Calculates the average of a variable number of arguments.

    Parameters:
    *args (float): A variable number of numerical arguments.

    Returns:
    float: The average of the provided numbers.
    """
    if not args:
        return 0  # Return 0 if no arguments are provided to avoid division by zero
    return sum(args) / len(args)


while True:
    try:
        user_input = int(input("Enter an integer: "))
        print("The number is:", classify_number(user_input))
        break  # Exit loop if valid input is provided
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

