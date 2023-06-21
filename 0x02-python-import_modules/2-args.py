#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    # Retrieve the arguments passed to the script
    args = sys.argv[1:]

    # Get the number of arguments
    num_args = len(args)

    # Print the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    # Print each argument with its position
    for i, arg in enumerate(args):
        print("{}: {}".format(i + 1, arg))
