def buddyStrings(a, b):
    """
    >>> ("ab", "ba")
    True
    
    >>> ("ab", "ab")
    False
    
    """
    switch_counter = 0
    i = 0
    
    if a == b or len(a) != len(b):
        return False

    for char, i in enumerate(a):
        if a[i] == b[i]:
            continue
        
    # while i < len(a) - 1:
    #     if a[i] == b[i]:
    #         continue
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()