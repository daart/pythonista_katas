def main(nums):
    """
    See https://leetcode.com/problems/single-element-in-a-sorted-array/
    You are given a sorted array consisting of only integers where every element appears exactly
    twice, except for one element which appears exactly once. Find this single element that appears
    only once.
    Follow up: Your solution should run in O(log n) time and O(1) space.
    >>> main([1, 1, 2, 3, 3, 4, 4, 8, 8])
    2
    >>> main([3, 3, 7, 7, 10, 11, 11])
    10
    >>> main([])
    >>> main([1])
    1
    >>> main([1, 1, 2])
    2
    """
    
    if len(nums) == 0:
        return
    
    res = []
    
    for num in nums:
        if len(res) > 1:
            return res[0]
            
        if num in res:
            res.pop()
        else:
            res.append(num)
    
    return res[0]

# test case nums = [] is a bit weird

if __name__ == "__main__":
    import doctest
    doctest.testmod() 