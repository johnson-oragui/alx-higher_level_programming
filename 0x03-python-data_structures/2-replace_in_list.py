#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        # Replace the element at the specified index
        my_list[idx] = element
        return my_list
