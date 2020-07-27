str1 = 'PAYPALISHIRING'
str2 = 'DATAROBOTISAWESOME'
    
def convert(s, numRows):
    """
    >>> convert('PAYPALISHIRING', 3)
    'PAHNAPLSIIGYIR'
    >>> convert('PAYPALISHIRING', 4)
    'PINALSIGYAHRPI'
    >>> convert('DATAROBOTISAWESOME', 3)
    'DRTWMAAOOIAEOETBSS'
    >>> convert('DATAROBOTISAWESOME', 4)
    'DBWAOOAEETRTSSMAIO'
    >>> convert('DATAROBOTISAWESOME', 5)
    'DTMAOIOETBSSAOAERW'
    """
    res = [''] * numRows
    step, row = -1, 0
    
    for char in s:
        res[row] += char
        # since we change direction when we hit bottom or top, we should change step to opposite
        if row % (numRows - 1) == 0:
            step = -step
        row += step
    
    return ''.join(res)


test1 = convert(str1, 3) # PAHNAPLSIIGYIR
test2 = convert(str1, 4) # PINALSIGYAHRPI
test3 = convert(str2, 3) # DRTWMAAOOIAEOETBSS
test4 = convert(str2, 4) # DBWAOOAEETRTSSMAIO
test5 = convert(str2, 5) # DTMAOIOETBSSAOAERW

if __name__ == "__main__":
    import doctest
    doctest.testmod() 