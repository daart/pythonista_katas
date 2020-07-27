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
    
    # great solution
    frequency_by_char = dict();
    for char in text:
        val = frequency_by_char[char] if char in frequency_by_char else 0
        frequency_by_char[char] = val + 1
    
    index_by_char = dict()
    for index, char in enumerate(text):
        if char not in index_by_char:
            index_by_char[char] = index
    
    triplets = [
        [freq, -index_by_char[char], char] 
        for char, freq in frequency_by_char.items()
    ]
    
    return ''.join([(char * freq) for freq, index, char in sorted(triplets, reverse=True)])
    
    # since sorting is the heavies operation here O(n logn)
    
    # super pythonista solution only for python v 3.6+ :)
    
    # char_collection = Counter(text).most_common()
    
    # return ''.join([key * val for key, val in char_collection])

def sort_letters_2(text):
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
    # only applicable for python 3.6+ version
    char_collection = Counter(text).most_common()
    return ''.join([key * val for key, val in char_collection]) 

def sort_letters_3(text):
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
    # with the help of collections.OrderedDict method
    if not len(text): return text
    
    char_dict = OrderedDict();
    for char in text:
        val = char_dict[char] if char in char_dict else 0
        char_dict[char] = val + 1
    
    sorted_char_dict = sorted(char_dict.items(), key=lambda char: char[1], reverse=True)
    
    return ''.join([key * val for key, val in sorted_char_dict]) 

if __name__ == "__main__":
    import doctest
    doctest.testmod() 