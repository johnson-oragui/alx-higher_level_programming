#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    # Check if the list is empty
    if len(my_list) == 0:
        # Return None if the list is empty
        return None
    
    # Initialize the maximum value to the first element of the list
    max_value = my_list[0]
    
    # Iterate over the remaining elements of the list
    for num in my_list[1:]:
        # Compare each element with the current maximum value
        if num > max_value:
            # If the current element is greater, update the maximum value
            max_value = num
    
    # Return the maximum value
    return max_value
