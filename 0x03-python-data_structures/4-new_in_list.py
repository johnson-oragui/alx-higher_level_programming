#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # Return a copy of the original list
        return my_list.copy()
    else:
        # Create a copy of the original list
        new_list = my_list.copy()
        # Replace the element at the specified index in the copy
        new_list[idx] = element
        # Return the modified copy
        return new_list
