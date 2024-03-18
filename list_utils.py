import math
from typing import List
from math import ceil

#1. read isntructions
#2. pseudoCode
#3. Google
#4. ChatCPT to not waste time on syntax

def get_item_at_position(list_in: List, pos: int) -> List:
    return list_in[pos]
    """
    Returns the item at pos.

    :param list_in: Input list
    :param pos: Position of desired item in list_in
    :return: Item in pos
    """
    # pass  # remove pass statement and implement me

def print_list_items(list_in: List) -> None:
    for item in list_in:
        print(item)


    """
    Given a list, this function iterates through it and prints each element.

    :param list_in: Input list
    :return: None
    """
    #pass  # remove pass statement and implement me


def sort_by_commit_count(list_in: List) -> List:
    list_in.sort(key=lambda x: x[1])
    return list_in
    """
    Given a list of entries, return a new list sorted based on the commit count.

    :param list_in: A list where each entry is a list containing a name and the commit count corresponding to a user
    :return: The same list sorted in ascending order based on the commit count
    """
    #RETURN A NEW LIST
    #USE BRACKETS FOR THE LIST
    #BASED ON THE COMMIT COUNT / COUNTER - ASCENDING

    #pass  # remove pass statement and implement me


def gen_list_of_nums(n: int) -> List[int]:
    return list(range (n))
    """
    Given a number (N), this function returns a list of integers from 0 to N (exclusive).
Return a list of integers from 0 to n (# of items in the list)
    :param n: The number of items the result should contain
    :return: A list of integers
    """
    #pass  # remove pass statement and implement me


def half_list(list_in: List, half: int) -> List:
    length = len(list_in)
    one_half = math.ceil(length/2)
    param_half1 = list_in[:one_half]
    if length % 2 != 0:
        half_two = list_in[one_half - 1:]

    else:
        half_two = list_in[one_half:]

    if half == 1:
        return param_half1

    elif half == 2:
        return half_two

    i =int(len.List %2)

    """
    Given a list, this function will return a new list that contains half of the items in the list_in parameter.

    :param list_in: The list which will be used to generate the RETURN value
    :param half: 1 will use the first half of the input list. 2 will use the second half of the input list.
    If the length of list_in is an odd number, round the half value up (hint: math.ceil()).
    :return: A list.
    """
    #pass  # remove pass statement and implement me


def remove_odds(list_in: List[int]) -> None:
    for (i) in list_in[:]:
        if (i % 2 != 0):
            list_in.remove(i)
    return list_in


def remove_evens(list_in: List[int]) -> None:
    for (i) in list_in[:]:
        if (i % 2 == 0):
            list_in.remove(i)
    return list_in

"""
    Given a list of integers, this function removes the odd numbers from the same list.
    #pass  # remove pass statement and implement me
    pass  # remove pass statement and implement me

"""

def concatenate_lists(list_a: List, list_b: List) -> List:
    list_c = list_a + list_b #forgot to _c on list_c otherwise I'd have had instant success
    return list_c

    """
    Given two lists, this function combines them and returns the result as a new list.
    :param list_a: A list
    :param list_b: Another list
    :return: A list containing all elements from list_a and list_b
    """
    pass  # remove pass statement and implement me



def multiply_list(list_in: List, scalar: int) -> List:
    product = list_in * scalar
    return product
    """
    Given a list and an integer, this function will return a new list which is the result of multiplying
    the input list by the value of the scalar.
    :param list_in: A list
    :param scalar: An integer
    :return: A list
    """
      # remove pass statement and implement me
