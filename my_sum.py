def my_sum(my_list):
    """Our version of the sum function.

    https://docs.python.org/dev/library/functions.html#sum

    This function takes a list of numbers and returns the sum of
    those numbers. This function should return 0 if the list is
    empty. We covered this in lecture, but see if you can write the
    function without referring to your notes.

    Arguments:
        my_list (list): A list of integers.

    Returns:
        int: The sum of all elements in my_list.

    Examples:

        >>> print(my_sum([]))
        0

        >>> print(my_sum([1, 2, 3]))
        6

        >>> print(my_sum([1.5, 2.5, 3.5]))
        7.5

    """
    i = 0
    sum_list = 0
    while i < len(my_list):
        sum_list += my_list[i]
        i += 1
    return sum_list
