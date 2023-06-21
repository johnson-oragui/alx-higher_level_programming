#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over each character in the string
    for char in my_string:
        # Check if the character is 'c' or 'C'
        if char != 'c' and char != 'C':
            # Append the character to the result string
            result += char
    
    # Return the resulting string
    return result
