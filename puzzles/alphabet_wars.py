"""
See https://www.codewars.com/kata/alphabet-war
== Introduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.
== Task
Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.
The left side letters and their power:
w - 4
p - 3
b - 2
s - 1
The right side letters and their power:
m - 4
q - 3
d - 2
z - 1
The other letters don't have power and are only victims.
"""

ARMIES = {
    'Left':  {
    'w': 4,
    'p': 3,
    'b': 2,
    's': 1,
    'y': 1,
}  
}

left_side_char_map = {
    'w': 4,
    'p': 3,
    'b': 2,
    's': 1,
    'y': 1,
}

right_side_char_map = {
    'm': 4,
    'q': 3,
    'd': 2,
    'z': 1,
    'y': 2,
}

center_army_map = {
    'a': 1,
    'u': 1,
    'i': 1,
    'e': 1,
    'o': 1,
}

def calc_total_score(army, text):
    return sum([
        army[char] 
        for char in text 
        if char in army
    ])
    
def accum_result(left_total_score, right_total_score, central_total_score):
    l_side, r_side, c_side, final_statement, draw = 'Left', 'Right', 'Central', ' side wins!', 'Let\'s fight again!'
    
    final_statement_dict = {
        'Left': left_total_score,  
        'Right': right_total_score,  
        'Central': central_total_score,  
    }
    
    buffer = []
    for key, val in final_statement_dict.items():
        buffer.append([val, key])
    buffer.sort()
    
    last, prev = buffer[-1], buffer[-2]
    
    if last[0] > prev[0]:
        return last[1] + final_statement
    else:
        return draw
    
    # max_val = 0
    # winner = ''
    
    # for key, val in final_statement_dict.items():
    #     if val > max_val:
    #         max_val = val
    #         winner = key
    
    # if winner == '':
    #     return draw
    
    # return winner + final_statement
    
    # if left_total_score > right_total_score:
    #     return l_side + final_statement
    # elif right_total_score > left_total_score:
    #     return r_side + final_statement
    # else:
    #     return draw

def fight(text):
    """
    >>> fight('')
    "Let's fight again!"
    >>> fight('abracadabra')
    'Left side wins!'
    >>> fight('z')
    'Right side wins!'
    >>> fight('zdqmwpbs')
    "Let's fight again!"
    >>> fight('zzzzs')
    'Right side wins!'
    >>> fight('wwwwwwz')
    'Left side wins!'
    >>> fight('bdy')
    'Right side wins!'
    """
    winner = ''
    left_total_score, right_total_score, center_army_score = 0, 0, 0
    
    for char in text:
        if (char in left_side_char_map):
            left_total_score += left_side_char_map[char]
    
    left_total_score = calc_total_score(left_side_char_map, text)
    right_total_score = calc_total_score(right_side_char_map, text)
    center_army_score = calc_total_score(center_army_map, text)
            
    return accum_result(left_total_score, right_total_score)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
