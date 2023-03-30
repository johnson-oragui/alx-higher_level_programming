#!/usr/bin/python3

def magic_calculation(a, b):
    '''Performs calculations between two integers

    Args:
        a: The first integer
        b: The second integer

    Returns:
        If an error occurs - addition of integers
        otherwise - the desired result
    '''
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return (result)
