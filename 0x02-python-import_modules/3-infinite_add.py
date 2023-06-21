#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    # Retrieve the arguments passed to the script
    args = sys.argv[1:]

    # Initialize a variable to store the sum of the arguments
    sum_of_args = 0

    # Iterate over the arguments and add them to the sum
    for arg in args:
        sum_of_args += int(arg)

    # Print the result of the addition
    print(sum_of_args)
