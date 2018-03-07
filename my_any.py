def my_any(my_list):
    """Our version of the any function.

    https://docs.python.org/dev/library/functions.html#any

    This function takes a list, and returns True at least one
    element of the list is considered True. This function should
    return False if the list is empty.

    Arguments:
        my_list (list): A list of integers and strings.

    Returns:
        bool: True if any element of my_list is considered True.
            False otherwise.

    Examples:

        >>> print(my_any([]))
        False

        >>> print(my_any([1, 'hello', [1, 2, 3]]))
        True

        >>> print(my_any([0, '', []]))
        False

        >>> print(my_any([1, '', []]))
        True

        >>> print(my_any([1, 'hello', []]))
        True

        >>> print(my_any([1, '', [1, 2, 3]]))
        True

    """
    i = 0
    while i < len(my_list):
        if my_list[i]:
            return True
        else:
            i += 1
    return False