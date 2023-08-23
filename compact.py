def compact(lst):
    for item in lst:
        if item == False:
            lst.remove(item)
    return lst

    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """