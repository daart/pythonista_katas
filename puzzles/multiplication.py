from functools import reduce

def multiplier(a, b):
    return a * b

def main(numbers):
    """
    Given a sequence of integers. Build a new sequence of the same length. Each element of a new
    sequence should be calculated as a multiplication of elements of the original sequence except
    the element with the same index.  Think about possible corner cases.
    >>> main([1, 5, 3])
    [15, 3, 5]
    >>> main([1, 2, 2, 5, 8])
    [160, 80, 80, 32, 20]
    """
    total = reduce(multiplier, numbers)
        
    return [total // val for val in numbers ]
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()