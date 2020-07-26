str1 = 'PAYPALISHIRING'
str2 = 'DATAROBOTISAWESOME'

def calc_total_cols(rows, stringLen):
    tot_full_cols = stringLen // rows
    in_between_cols = rows - 2
    tot_in_between_cols = in_between_cols * (tot_full_cols - 1)
    
    return tot_full_cols + tot_in_between_cols

def build_matrix(size):
    r, c = size
    return [['' for col in range(c)] for row in range(r)]

def fill_matrix(matrix, word):
    current_word_i, r, c, r_lim, c_lim = 0, 0, 0, len(matrix) - 1, len(matrix[0]) - 1
    
    while current_word_i < len(word):
        if r == r_lim:
            while r > 1:
                c += 1
                r -= 1
                matrix[r][c] = word[current_word_i]
                current_word_i += 1
            c += 1
        elif r == 0:

            while r <= r_lim:
                if current_word_i == len(word): 
                    break
                matrix[r][c] = word[current_word_i]
                r += 1
                current_word_i += 1
        r -= 1
    
    return matrix
    
    
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
    
    # suuuper noob solution
    numCols = calc_total_cols(numRows, len(s))
    matrix = build_matrix([numRows, numCols])
    
    temp_res = fill_matrix(matrix, s)
    
    final_res = ''.join(''.join(row).strip() for row in temp_res)
    return final_res


test1 = convert(str1, 3) # PAHNAPLSIIGYIR
test2 = convert(str1, 4) # PINALSIGYAHRPI
test3 = convert(str2, 3) # DRTWMAAOOIAEOETBSS
test4 = convert(str2, 4) # DBWAOOAEETRTSSMAIO
test5 = convert(str2, 5) # DTMAOIOETBSSAOAERW

if __name__ == "__main__":
    import doctest
    doctest.testmod() 