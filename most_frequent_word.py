import random
def most_frequent_word(text):
    """
    >>> most_frequent_word('i think therefore i am')
    'i'
    >>> most_frequent_word("be the change that you wish to see in the world")
    'the'
    >>> most_frequent_word("i therefore am think am therefore am think therefore am")
    'am'
    >>> most_frequent_word("i think am therefore am therefore am think therefore")
    'am'
    """
    if len(text) == 0:
        return text

    formatted = text.split(' ')
    word_dict = dict()
    max_word_count = 0

    for word in formatted:
        value = word_dict[word] if word in word_dict else 0 # word_dict.get word_dict.setdefault !!!
        word_dict[word] = value + 1

    def key(element): return word_dict[element]
    key = lambda el: word_dict[el]

    sorted_word_winners = sorted([[value, key] for key, value in word_dict.items()], reverse = True)
    # TODO redo word_dictionary so the key becomes a value and vice versa
    # TODO from collections inport Counter !!!
    
    return sorted_word_winners[:10]

    # return max(word_dict, key = lambda word: word_dict[word])


test1 = most_frequent_word('i think therefore i am')
test2 = most_frequent_word("be the change that you wish to see in the world")
test3 = most_frequent_word("I therefore am think am therefore am think therefore am")
test4 = most_frequent_word("I therefore am think am therefore am think therefore")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
