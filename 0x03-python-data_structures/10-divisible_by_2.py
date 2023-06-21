#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    # Create a new list to store the True/False values
    result = []
    
    # Iterate over the elements of the original list
    for num in my_list:
        # Check if the element is divisible by 2
        if num % 2 == 0:
            # Append True if divisible by 2
            result.append(True)
        else:
            # Append False if not divisible by 2
            result.append(False)
    
    # Return the new list with True/False values
    return result
