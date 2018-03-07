def my_count(my_list, my_element):
    """Our version of the count function.

    https://docs.python.org/dev/library/stdtypes.html#common-sequence-operations

    This function takes a list and an element, and returns the number
    of times that element appears in the list.

    Arguments:
        my_list (list): A list of integers.
        my_element (int): The element to be counted.

    Returns:
        int: The number of times my_element appears in my_list.

    Examples:

        >>> print(my_count([], 1))
        0

        >>> print(my_count([1, 2, 3], 2))
        1

        >>> print(my_count([1, 2, 3], 4))
        0

        >>> print(my_count([3, 1, 2, 3, 1], 2))
        1

        >>> print(my_count([3, 1, 2, 3, 1], 3))
        2

    """
    i = 0
    count_list = 0
    while i < len(my_list):
        if my_element == my_list[i]:
            count_list += 1
            i += 1
        else:
            count_list = count_list
            i += 1
    return count_list