#!/usr/bin/python3
def magic_calculation(a, b):
    """
    Perform a magic calculation based on the given values
    """

    # Import the 'add' and 'sub' functions 
    # from the 'magic_calculation_102' module
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    # Check if 'a' is less than 'b'
    if a < b:
        # Perform addition and store the result in 'c'
        c = add(a, b)

        # Perform addition multiple times using a loop
        for i in range(4, 6):
            c = add(c, i)

        # Return the final result
        return c
    else:
        # Perform subtraction and return the result
        return sub(a, b)
