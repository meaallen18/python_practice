def mode(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    max_freq = 0
    mode_val = None
    for num, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            mode_val = num
    return mode_val



    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
