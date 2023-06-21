#!/usr/bin/python3

def delete_at(my_list=None, idx=0):
    """Delete an item at a specific position in a list."""
    if my_list is None:
        # Set an empty list if my_list is None
        my_list = []

    if 0 <= idx < len(my_list):
        # Remove the item at the specified index using the del statement
        del my_list[idx]
    # Return the modified list
    return my_list
