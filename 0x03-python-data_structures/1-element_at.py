#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrive an element from a list."""
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        # Return the element at the specified index
        return my_list[idx]
