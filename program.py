def calculate_mean(numbers):
    """
    Calculates the mean (average) of a list of numbers.

    Args:
        numbers: A list of numbers (integers or floats).

    Returns:
        The mean of the numbers, or None if the input list is empty.
        Raises a TypeError if the input is not a list or if the list
        contains non-numeric elements.
    """

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not numbers:  # Check for empty list
        return None

    total = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("List elements must be numeric")
        total += number

    mean = total / len(numbers)
    return mean


# Example Usage:
list1 = [1, 2, 3, 4, 5]
mean1 = calculate_mean(list1)
print(f"Mean of {list1}: {mean1}")  # Output: Mean of [1, 2, 3, 4, 5]: 3.0

list2 = [10.5, 20.2, 30.7, 40.1]
mean2 = calculate_mean(list2)
print(f"Mean of {list2}: {mean2}") # Output: Mean of [10.5, 20.2, 30.7, 40.1]: 25.375

empty_list = []
mean_empty = calculate_mean(empty_list)
print(f"Mean of {empty_list}: {mean_empty}") # Output: Mean of []: None

# Example of error handling:
try:
    mean_error = calculate_mean([1, 2, "a", 4])  # List with a string
    print(mean_error)
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: List elements must be numeric

try:
    mean_error2 = calculate_mean("not a list")
    print(mean_error2)
except TypeError as e:
    print(f"Error: {e}") # Output: Error: Input must be a list