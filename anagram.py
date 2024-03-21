def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    if len(first_string) != len(second_string):
        return False

    list_a = list(first_string)
    list_b = list(second_string)

    for i in first_string:
            if i in list_a and i in list_b:
                list_a.remove(i)
                list_b.remove(i)
            else:
                return False

    return True
