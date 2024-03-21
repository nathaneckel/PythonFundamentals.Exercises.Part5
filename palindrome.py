def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    sanitized_input = value.lower().replace(" ","")
    reversed_sanitized_input = reversed(sanitized_input)

    a = list(sanitized_input)
    b = list(reversed_sanitized_input)

    return a == b

    #pass  # remove pass statement and implement me
