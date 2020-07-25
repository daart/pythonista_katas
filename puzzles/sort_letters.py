from collections import Counter, OrderedDict
from operator import itemgetter, attrgetter

def sort_letters(text):
    """
    >>> sort_letters('aaabccccdeefffff')
    'fffffccccaaaeebd'
    >>> sort_letters('aaadccccbeefffff')
    'fffffccccaaaeedb'
    >>> sort_letters('abcdefghijklmnop')
    'abcdefghijklmnop'
    >>> sort_letters('')
    ''
    >>> sort_letters('aba')
    'aab'
    >>> sort_letters('abcabccba')
    'aaabbbccc'
    """
    
    if not len(text): return text
    
    # noob solution
    char_dict = OrderedDict();
    
    for char in text:
        val = char_dict[char] if char in char_dict else 0
        char_dict[char] = val + 1
    
    sorted_char_dict = sorted(char_dict.items(), key=lambda char: char[1], reverse=True)
    
    return ''.join([key * val for key, val in sorted_char_dict]) 
    
    # since sorting is the heavies operation here O(n logn)
    
    # super pythonista solution only for python v 3.6+ :)
    
    # char_collection = Counter(text).most_common()
    
    # return ''.join([key * val for key, val in char_collection])
    
test1 = sort_letters('aaadccccbeefffff')

print(test1)

if __name__ == "__main__":
    import doctest
    doctest.testmod() 