#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples"""
    # Create new tuples with default values of 0
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Take the first two integers from each tuple and add them
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]

    # Return a tuple with the computed sums
    return sum_1, sum_2
