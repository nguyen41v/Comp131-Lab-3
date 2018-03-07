def my_enumerate(my_list):
    """Our version of the enumerate function.

    https://docs.python.org/dev/library/functions.html#enumerate

    This function takes a list, and returns a nested list, where each
    inner list contains the index and the element of the original
    list at that index.

    Arguments:
        my_list (list): A list of integers and strings.

    Returns:
        list: A list of lists, with each inner list containing the index
            and the element of each item in my_list.

    Examples:

        >>> print(my_enumerate([]))
        []

        >>> print(my_enumerate(['a', 'b', 'c']))
        [[0, 'a'], [1, 'b'], [2, 'c']]

    """


    i = 0
    my_enumerate = []
    if len(my_list) > 0:
        while i < len(my_list):
            my_enumerate += [[i , my_list[i]]]
            i += 1
        return my_enumerate
    else:
        return []