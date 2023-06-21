#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for row in matrix:
        # Iterate over each element in the row
        for num in row:
            # Print the number with a space separator and no newline
            print("{:d}".format(num), end=" ")
        # Print a newline after each row
        print()
