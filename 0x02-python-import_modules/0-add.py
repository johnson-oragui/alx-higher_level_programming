#!/usr/bin/python3
if __name__ == "__main__":
    """ Module to add two integers. """
    from add_0 import add

    # Assign the value 1 to the variable 'a'
    a = 1

    # Assign the value 2 to the variable 'b'
    b = 2

    # Call the 'add' function from the 'add_0' module with 'a' and 'b' as arguments
    result = add(a, b)

    # Print the formatted string showing the addition result
    print("{} + {} = {}".format(a, b, result))

