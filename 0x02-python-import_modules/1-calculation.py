#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient ofintegers"""
    from calculator_1 import add, sub, mul, div

    # Assign the value 10 to the variable 'a'
    a = 10

    # Assign the value 5 to the variable 'b'
    b = 5

    # Perform addition using the 'add' function
    result_add = add(a, b)

    # Perform subtraction using the 'sub' function
    result_sub = sub(a, b)

    # Perform multiplication using the 'mul' function
    result_mul = mul(a, b)

    # Perform division using the 'div' function
    result_div = div(a, b)

    # Print the result of addition
    print("{} + {} = {}".format(a, b, result_add))

    # Print the result of subtraction
    print("{} - {} = {}".format(a, b, result_sub))

    # Print the result of multiplication
    print("{} * {} = {}".format(a, b, result_mul))

    # Print the result of division
    print("{} / {} = {}".format(a, b, result_div))
