def my_zip_advanced(lists):
    """
    >>> print(my_zip_advanced([[], []]))
    []
    >>> print(my_zip_advanced([ [1, 2, 3] ]))
    [[1], [2], [3]]
    >>> print(my_zip_advanced([ [1, 2, 3], ['a', 'b', 'c'] ]))
    [[1, 'a'], [2, 'b'], [3, 'c']]
    >>> print(my_zip_advanced([ [1, 2, 3, 4, 5], ['a', 'b', 'c'] ]))
    [[1, 'a'], [2, 'b'], [3, 'c']]
    >>> print(my_zip_advanced([ [1, 2, 3], ['a', 'b', 'c', 'd', 'e'] ]))
    [[1, 'a'], [2, 'b'], [3, 'c']]
"""
    i_of_list_in_list = 0
    my_total_zip = []
    short_i = 1
    my_min = len(lists[0])
    if len(lists) > 0:
        while short_i < len(lists):
            if my_min <= len(lists[short_i]):
                short_i += 1
            else:
                my_min = len(lists[short_i])
                short_i += 1
        while i_of_list_in_list < my_min:
            n = 0
            my_zip = []
            while n < len(lists):
                my_zip += lists[n][i_of_list_in_list: i_of_list_in_list + 1]
                n += 1
            my_total_zip += [my_zip]
            i_of_list_in_list += 1

    return my_total_zip

print(my_zip_advanced([[1, 2, 3, 4],["a", "b", "c"], [4, 5, 6]]))
print(my_zip_advanced([[1, 2, 3], ['a', 'b', 'c', 'd', 'e']]))
print(my_zip_advanced([[1, 2, 3], ['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4],["a", "b", "c"], [4, 5, 6]]))
print(my_zip_advanced([
    [1, 2, 3, 4],
    ['one', 'two', 'three', 'four', 'five', 'six', 'seven'],
    ['yi', 'er', 'san', 'si', 'wu']
]))



