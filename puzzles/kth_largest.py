def kth_largest(numbers, k):
    """
    See https://leetcode.com/problems/kth-largest-element-in-an-array/
    >>> kth_largest([3, 2, 1, 5, 6, 4], 2)
    5
    >>> kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4
    >>> kth_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    9
    >>> kth_largest([10, 9, 5, 6, 4, 7, 2, 1, 3, 8], 3)
    8
    """

    res = [0] * k
    min = 0
    # how to fill the list when it's empty
    # temp min value
    # how to switch prev min element with the new min

    for num in numbers:
        if num > min(res):
            res.append(num)
