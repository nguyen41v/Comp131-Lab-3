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
    if len(my_list) > 0:
        while (i) < len(my_list):
            my_reversed += my_list[len(my_list) - 1 - i:len(my_list) - i]
            i += 1
        return my_reversed
    else:
        return my_reversed


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