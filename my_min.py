def my_min(my_list):
    """Our version of the min function.

    https://docs.python.org/dev/library/functions.html#min

    This function takes a list of numbers and returns the smallest
    of those numbers. You may assume the list is not empty, but you
    may *not* assume that it will only contain positive numbers.

    Arguments:
        my_list (list): A list of integers.

    Returns:
        int: The smallest element in my_list.

    Examples:

        >>> print(my_min([1, 2, 3]))
        1

        >>> print(my_min([1, 1, 2, 3, 1]))
        1

    """
    i = 0
    my_min = my_list[0]
    while i < len(my_list):
        if my_min < my_list[i]:
            i += 1
        else:
            my_min = my_list[i]
            i += 1
    return my_min