#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for row in matrix:
        # Iterate over the elements in the row
        for i, num in enumerate(row):
            # Check if the current element is the last element in the row
            if i == len(row) - 1:
                # Print the number without a space at the end
                print("{:d}".format(num), end="")
            else:
                # Print the number followed by a space
                print("{:d} ".format(num), end="")
        # Move to the next line after printing all elements of a row
        print()

