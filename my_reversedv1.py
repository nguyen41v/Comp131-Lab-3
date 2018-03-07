def my_reversed(my_list):
    """Our version of the reversed function.

    https://docs.python.org/dev/library/functions.html#reversed

    This function takes a list, and returns a list that contains
    the same elements in reverse.

    Arguments:
        my_list (list): A list of integers and strings.

    Returns:
        list: The elements of my_list, in reverse.

    Examples:

        >>> print(my_reversed([]))
        []

        >>> print(my_reversed([1, 2, 3]))
        [3, 2, 1]

        >>> print(my_reversed([1, 'a', 3, 2, 'z']))
        ['z', 2, 3, 'a', 1]

    """
    i = 0
    my_reversed = []
    while i < len(my_list):
        my_reversed += my_list[len(my_list) - 1 - i:len(my_list) - i]
        i += 1
    return my_reversed
