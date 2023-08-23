def last_element(lst):
    if lst:  # Check if list is not empty
        return lst[-1]
    else:
        return None



    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """