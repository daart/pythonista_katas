
def merge(intervals):
    """
    >>> merge([[1,3],[2,6],[8,10],[15,18]])
    [[1, 6], [8, 10], [15, 18]]

    >>> merge([[1,4],[4,5]])
    [[1, 5]]

    >>> merge([[1,4],[5,6]])
    [[1, 4], [5, 6]]

    >>> merge([[1,4]])
    [[1, 4]]

    >>> merge([[1, 4], [0, 5]])
    [[0, 5]]

    >>> merge([[1, 4], [0, 0]])
    [[0, 0], [1, 4]]

    >>> merge([[1,4], [0, 2], [3, 5]])
    [[0, 5]]

    >>> merge([[1,4], [2, 3]])
    [[1, 4]]

    >>> merge([[1,4], [6, 8], [10, 14], [11, 15]])
    [[1, 4], [6, 8], [10, 15]]

    >>> merge([[1,3], [2, 6], [6, 8], [10, 14], [11, 15]])
    [[1, 8], [10, 15]]
    """

    if len(intervals) == 0:
        return intervals

    # prev_indice = 0
    # next_indice = prev_indice + 1

    sorted_intervals = sorted(intervals)
    res = []
    merge_buffer = sorted_intervals[0]

    for i_start, i_end in sorted_intervals[1:]:
        m_start, m_end = merge_buffer

        if m_end >= i_start:
            merge_buffer = [m_start, max(m_end, i_end)]

        else:
            res.append(merge_buffer)
            merge_buffer = [i_start, i_end]

    # while prev_indice < len(sorted_intervals) - 1:
    #     if merge_buffer[1] >= sorted_intervals[next_indice][0]:
    #         merge_buffer = [merge_buffer[0], max(
    #             merge_buffer[1], sorted_intervals[next_indice][1])]
    #
    #     else:
    #         res.append(merge_buffer)
    #         merge_buffer = sorted_intervals[next_indice]
    #
    #     prev_indice = next_indice
    #     next_indice += 1
    #

    res.append(merge_buffer)

    return res


test1 = merge([[1, 3], [2, 6], [8, 10], [15, 18]]) # [[1, 6], [8, 10], [15, 18]]
test2 = merge([[1, 4], [4, 5]]) # [[1, 5]]
test3 = merge([[1, 4], [5, 6]])  # [[1,4],[5,6]]
test4 = merge([[1, 4]])  # [[1, 4]]
test5 = merge([[1, 4], [0, 5]])  # [[0, 5]]
test6 = merge([[1, 4], [0, 0]])  # [[0, 0], [1, 4]]
test7 = merge([[1, 4], [0, 2], [3, 5]])  # [[0, 5]]
test8 = merge([[1, 4], [2, 3]])  # [[1, 4]]
test9 = merge([[1, 4], [6, 8], [10, 14], [11, 15]])# [[1, 4], [6, 8], [10, 15]]
test10 = merge([[1, 3], [2, 6], [6, 8], [10, 13], [12, 15]]) # [[1, 8], [10, 15]]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
