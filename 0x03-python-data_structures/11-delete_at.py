#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    # Create a new list and copy the elements before the specified index
    new_list = my_list[:idx]

    # Copy the elements after the specified index
    new_list.extend(my_list[idx + 1:])

    # Return the new list with the item at the specified index removed
    return new_list
