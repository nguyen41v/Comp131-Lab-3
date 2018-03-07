def my_zip_beginner(my_list_1, my_list_2):
    """Our version of a two-argument version of the zip function.

    https://docs.python.org/dev/library/functions.html#zip

    This function takes two lists, and returns a list, with a
    list containing the first elements of both lists as the first
    element, a list containing the second elements of both lists
    as the second element, and so on. You may assume that the two
    lists are of equal length.

    Arguments:
        my_list_1 (list): A list of integers or strings.
        my_list_2 (list): A list of integers or strings.

    Returns:
        list: A list of lists, with each inner list containing the
            corresponding elements from my_list_1 and my_list_2.

    Examples:

        >>> print(my_zip_beginner([], []))
        []

        >>> print(my_zip_beginner([1, 2, 3], ['a', 'b', 'c']))
        [[1, 'a'], [2, 'b'], [3, 'c']]

    """
    i = 0
    my_zip = []
    if len(my_list_1) > 0:
        while i < len(my_list_1):
            my_zip += [[my_list_1[i], my_list_2[i]]]
            i += 1
        return my_zip
    else:
        return []