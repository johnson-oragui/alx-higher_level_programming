#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    # Check if the sentence is empty
    if sentence == "":
        # Return a tuple with length 0 and None as the first character
        return 0, None
    
    # Retrieve the length of the sentence using len()
    length = len(sentence)
    
    # Retrieve the first character of the sentence
    first = sentence[0]
    
    # Return a tuple with the length and the first character
    return length, first
