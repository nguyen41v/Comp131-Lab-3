def my_all(my_list):
    """Our version of the all function.

    https://docs.python.org/dev/library/functions.html#all

    This function takes a list, and returns True only if every
    element of the list is considered True. This function should
    return True if the list is empty.

    Arguments:
        my_list (list): A list of integers and strings.

    Returns:
        bool: True if all elements of my_list are considered True.
            False otherwise.

    Examples:

        >>> print(my_all([]))
        True

        >>> print(my_all([1, 'hello', [1, 2, 3]]))
        True

        >>> print(my_all([0, '', []]))
        False

        >>> print(my_all([1, '', []]))
        False

        >>> print(my_all([0, 'hello', []]))
        False

        >>> print(my_all([0, '', [1, 2, 3]]))
        False

    """
    i = 0
    while i < len(my_list):
        if my_list[i]:
            i += 1
        else:
            return False
    return True