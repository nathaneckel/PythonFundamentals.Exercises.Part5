
# def str_len(str_in: str) -> str:
def str_len(str_in: str) -> str:
    return len(str_in)
"""
Given a string parameter, this function should return the length of the parameter.
"""
  # remove pass statement and implement me


def first_char(str_in: str) -> str:
    return str_in[0]
"""
Given a string parameter, this function should return the first letter of the parameter.
"""
    # pass  # remove pass statement and implement me


def last_char(str_in: str) -> str:
    return str_in[-1]
"""
Given a string parameter, this function should return the last letter of the parameter..
"""
    # pass  # remove pass statement and implement me


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    return sub_str_in in str_in
"""
This function determines if the substring exists within the string. Returns True or False.
"""


def substring(str_in: str, start: int, stop: int) -> str:
    return str_in[start: stop]

"""
Returns the substring of a string.

Keyword arguments:
str_in -- the string in which to generate a substring from
start -- starting position of the input parameter to start the substring (inclusive)
stop -- stopping position of the input parameter to stop the substring (exclusive)
"""


def opposite_case(str_in: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """
    result = []
    for letter in str_in:
        if letter.isupper():
            result.append(letter.lower())
        else:
            result.append(letter.upper())
    return "".join(result)

#makes sense, if letter isUPPER (lower it
# if letter ISlower UPPER it
# then "".JOIN(result)