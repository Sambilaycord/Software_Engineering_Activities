import random

""" Bug Fix Explanation:
    Previously, the calculate_average function would raise a ZeroDivisionError 
    if given an empty list, since it attempted to divide by len(numbers).
    This was fixed by adding a check: if the list is empty, return 0 instead.
"""

def calculate_average(numbers):
    """Calculates the average of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The average of the numbers, or 0 if the list is empty.
    """
    if not numbers:
        return 0

    total = 0
    for number in numbers:
        total += number 
    return total / len(numbers)  


def generate_random_numbers(count, max_value):
    """Generates a list of random numbers.

    Args:
        count: The number of random numbers to generate.
        max_value: The maximum value for the random numbers.

    Returns:
        A list of random numbers.
    """
    random_numbers = []
    for _ in range(count):
        random_numbers.append(random.randint(0, max_value))
    return random_numbers


def main():
    """Main function to demonstrate the average calculation."""
    num_count = 0 
    max_rand_value = 0  
    
    random_nums = generate_random_numbers(num_count, max_rand_value)

    average = calculate_average(random_nums)

    print("Random Numbers:", random_nums)
    print("Average:", average)


if __name__ == "__main__":
    main()