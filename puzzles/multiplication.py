from functools import reduce
from collections import Counter

def multiplier(a, b):
    return a * b

def main(numbers):
    """
    Given a sequence of integers. Build a new sequence of the same length. Each element of a new
    sequence should be calculated as a multiplication of elements of the original sequence except
    the element with the same index.  Think about possible corner cases.
    
    Possible corner cases:
    1) if integer is 0
    2) if integer is < 0
    3) if multiplication result is > Integer.MAX_VALUE
    
    >>> main([1, 5, 3])
    [15, 3, 5]
    >>> main([1, 2, 2, 5, 8])
    [160, 80, 80, 32, 20]
    >>> main([1, 2, 5, 0, 8])
    [0, 0, 0, 80, 0]
    >>> main([0, 2, 5, 2, 8])
    [160, 0, 0, 0, 0]
    >>> main([1, 2, 0, 5, 0])
    [0, 0, 0, 0, 0]
    """
    
    counter = Counter(numbers)
    if counter[0] > 1:
        return [0] * len(numbers)
    if counter[0] == 1:
        zero_index = numbers.index(0)  
        return [0] * zero_index + [reduce(multiplier, numbers[: zero_index] + numbers[zero_index + 1: ])] + [0] * (len(numbers) - zero_index - 1)
    total = reduce(multiplier, numbers)
        
    return [total // val for val in numbers ]
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()