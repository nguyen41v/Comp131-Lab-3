def my_index_1(my_list, my_element):
    """Our version of the one-argument version of the index function.

    https://docs.python.org/dev/library/stdtypes.html#common-sequence-operations

    This function takes a list and an element, and returns the smallest
    index where the element occurs in the list. This function returns
    None if the element is not in the list.

    Arguments:
        my_list (list): A list of integers.
        my_element (int): The element to be found.

    Returns:
        int: The smallest index at which my_element is found in my_list.

    Examples:

        >>> print(my_index_1([], 2))
        None

        >>> print(my_index_1([1, 2, 3], 2))
        1

        >>> print(my_index_1([3, 1, 2, 3, 1], 2))
        2

        >>> print(my_index_1([3, 1, 2, 3, 1], 3))
        0

    """
    i = 0
    valid = 0
    if len(my_list) > 0:
        while valid == 0:
            if my_element == my_list[i]:
                valid = 1
                return i
            else:
                i += 1
                if i == len(my_list) - 1:
                    valid = 1
    return


def my_index_1(my_list, my_element):
    """
    can do with enumerate and for loop
    for i,e in enumerate(my_list):
        if e == my_element:
            return i
    return
    """
    pass