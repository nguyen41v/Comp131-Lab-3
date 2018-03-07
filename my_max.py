def my_max(my_list):
    """Our version of the max function.

    https://docs.python.org/dev/library/functions.html#max

    This function takes a list of numbers and returns the largest
    of those numbers. You may assume the list is not empty and that
    it will only contain positive numbers.

    Arguments:
        my_list (list): A list of integers.

    Returns:
        int: The largest element in my_list.

    Examples:

        >>> print(my_max([1, 2, 3]))
        3

        >>> print(my_max([1, 1, 2, 3, 1]))
        3

    """
    i = 0
    my_max = 0
    while i < len(my_list):
        if my_max < my_list[i]:
            my_max += my_list[i]
            i += 1
        else:
            my_max = my_max
            i += 1
    return my_max