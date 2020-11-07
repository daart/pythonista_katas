from collections import defaultdict
"""
See https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

grid = [
    [A B C E],
    [S F C S],
    [A D E E],
]

"ABCCED" => True
"SEE" => True
"ABCBQ" => False
"""

# Solution from me
class Trie:
    def __init__(self):
        self.root = dict()
        self.end = '*'

    def add(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = dict()
            node = node[letter]
        node[self.end] = None


class Solution:
    def get_neighbors(self, i, j, board):
        neighbors = list()
        if i > 0:
            neighbors.append([i - 1, j])

        if j > 0:
            neighbors.append([i, j - 1])

        if i < len(board) - 1:
            neighbors.append([i + 1, j])

        if j < len(board[0]) - 1:
            neighbors.append([i, j + 1])

        return neighbors

    def find(self, board, row, col, trieNode, visited):
        if visited[row][col]:
            return

        current_letter = board[row][col]

        if current_letter not in trieNode:
            return

        trieNode = trieNode[current_letter]
        visited[row][col] = True

        if '*' in trieNode:
            return True

        neighbors = self.get_neighbors(row, col, board)

        for neighbor_coords in neighbors:
            if self.find(
                board,
                neighbor_coords[0],
                neighbor_coords[1],
                trieNode,
                visited,
            ):
                return True

        visited[row][col] = False

    def exist(self, board, word):
        trie = Trie()
        trie.add(word)
        visited = [[False for _ in row] for row in board]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.find(board, i, j, trie.root, visited):
                    return True

        return False


class Trie:
    def __init__(self):
        self.trie = dict()

    def __repr__(self):
        return str(self.trie)

    def add(self, word):
        if len(word) == 0:
            self.trie[''] = None
        else:
            if word[0] not in self.trie:
                nested_trie = Trie()
                self.trie[word[0]] = nested_trie
            else:
                nested_trie = self.trie[word[0]]
            nested_trie.add(word[1:])


def get_neighbours(board, x, y):
    """
    >>> get_neighbours([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0)
    [(1, 0), (0, 1)]
    >>> get_neighbours([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1)
    [(0, 1), (2, 1), (1, 0), (1, 2)]
    """
    result = []
    # up
    if x > 0:
        value = (x - 1, y)
        result.append(value)
    # bottom
    if x < len(board) - 1:
        value = (x + 1, y)
        result.append(value)
    # left
    if y > 0:
        value = (x, y - 1)
        result.append(value)
    # right
    if y < len(board[0]) - 1:
        value = (x, y + 1)
        result.append(value)
    return result


def build_word(board, path):
    res = ''
    for x, y in path:
        res += board[x][y]
    return res


def build_trie(words):
    root = Trie()
    for w in words:
        root.add(w)

    return root


class Solution:
    def __init__(self, board, words):
        self.board = board
        self.words = words

    def find_all(self):
        result = []
        root = build_trie(self.words)
        for row_index in range(len(self.board)):
            for col_index in range(len(self.board[0])):
                letter = self.board[row_index][col_index]
                if letter in root.trie:  # todo: __contains__
                    path = [(row_index, col_index)]
                    # todo: __getitem__
                    res = self.find(row_index, col_index,
                                    root.trie[letter], path)
                    result.extend(res)
        return result

    def find(self, row, col, root, visited):
        result = []
        # todo: reccursion stop
        # todo: what if we have a completed word already?
        # traverse matrix
        if '' in root.trie:
            word = build_word(self.board, visited)
            x, y = visited[0]  # starting point
            result.append((word, x, y))

        connected = get_neighbours(self.board, row, col)
        # todo: except visited cells
        candidates = []
        for cell in connected:
            if cell not in visited:
                candidates.append(cell)
        # if current grid_char doesn't equal to current word_char
        for x, y in candidates:
            char = self.board[x][y]
            # for each connected: run reccursive search
            if char in root.trie:
                visited.append((x, y))
                res = self.find(x, y, root.trie[char], visited)
                result.extend(res)
                visited.pop()
        return result


def test_solution():
    words = ['foo', 'bar', 'foobar', 'baz']
    board = [
        'foob',
        'oora',
        'zzzz',
    ]

    solution = Solution(board, words)
    results = solution.find_all()
    assert len(results) == 6, results


def test_solution_on_big_data(n=1000):
    import string
    import random

    board = [[random.choice(string.ascii_lowercase)
              for _ in range(n)] for _ in range(n)]
    words = ['artem', 'ivan', 'olga']

    solution = Solution(board, words)
    results = solution.find_all()
    print(results)


def search(grid, word, index, row, col):
    # if we are out of boundary OR if current grid_char doesn't equal to current word_char
    is_out_of_x = row < 0 or row > len(grid) - 1
    is_out_of_y = col < 0 or col > len(grid[0]) - 1
    if is_out_of_x or is_out_of_y or grid[row][col] != word[index]:
        return False

    # if we are at the end of the target word
    if index == len(word) - 1:
        return True

    # mark already visited cell
    current_char, grid[row][col] = grid[row][col], ''
    # search through word 4ways
    if (
        search(grid, word, index + 1, row + 1, col) or
        search(grid, word, index + 1, row, col + 1) or
        search(grid, word, index + 1, row - 1, col) or
        search(grid, word, index + 1, row, col - 1)
    ):
        return True

    grid[row][col] = current_char

    return False


def main(board, word):
    """
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED")
    True
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "SEE")
    True
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "FBCCEE")
    True
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ADEESF")
    False
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCB")
    False
    >>> main([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCQ")
    False
    >>> main([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")
    True

    >>> main([["A"] * 1000] * 1000, "A" * 970)
    True
    """

    for r in range(len(board)):  # O(n)
        for c in range(len(board[0])):  # O(n)
            # for word in words:  # O(d)
            if word[0] == board[r][c] and search(board, word, 0, r, c):  # O(C)
                return True

    return False


"""
1 items had failures:
   8 of   8 in __main__.main
***Test Failed*** 8 failures.
('adding', 'fo', 'to', {})
('adding', 'o', 'to', {})
('adding', 'foo', 'to', {'f': <__main__.Trie instance at 0x10ac94640>})
('adding', 'oo', 'to', {'o': None})
Traceback (most recent call last):
  File "word_search.py", line 111, in <module>
    trie = build_trie(['fo', 'foo', 'food', 'bar'])
  File "word_search.py", line 43, in build_trie
    root.add(w)
  File "word_search.py", line 36, in add
    nested_trie.add(word[1:])
  File "word_search.py", line 36, in add
    nested_trie.add(word[1:])
AttributeError: 'NoneType' object has no attribute 'add'


1 items had failures:
   8 of   8 in __main__.main
***Test Failed*** 8 failures.
('adding', 'fo', 'to', {})
('adding', 'o', 'to', {})
('adding', '', 'to', {})
('adding', 'foo', 'to', {'f': {'o': {None: None}}})
('adding', 'oo', 'to', {'o': {None: None}})
('adding', 'o', 'to', {None: None})
('adding', '', 'to', {})
('adding', 'food', 'to', {'f': {'o': {'o': {None: None}, None: None}}})
('adding', 'ood', 'to', {'o': {'o': {None: None}, None: None}})
('adding', 'od', 'to', {'o': {None: None}, None: None})
('adding', 'd', 'to', {None: None})
('adding', '', 'to', {})
('adding', 'bar', 'to', {'f': {'o': {'o': {'d': {None: None}, None: None}, None: None}}})
('adding', 'ar', 'to', {})
('adding', 'r', 'to', {})
('adding', '', 'to', {})
{
    'b': {
        'a': {
            'r': {None: None}
        }
    },
    'f': {
        'o': {
            'o': {
                'd': {None: None},
                None: None
            },
            None: None
        }
    }
}

[('olga', 5, 842), ('olga', 6, 813), ('olga', 10, 790), ('olga', 13, 341), ('ivan', 21, 877), ('olga', 36, 226), ('ivan', 38, 996), ('ivan', 38, 996), ('ivan', 51, 124), ('olga', 53, 862), ('olga', 53, 862), ('ivan', 58, 348), ('ivan', 58, 348), ('artem', 58, 666), ('olga', 64, 12), ('olga', 69, 57), ('ivan', 73, 102), ('olga', 75, 174), ('artem', 77, 362), ('olga', 84, 158), ('ivan', 93, 445), ('olga', 100, 143), ('ivan', 108, 604), ('ivan', 111, 595), ('ivan', 112, 303), ('ivan', 118, 632), ('artem', 129, 589), ('ivan', 132, 127), ('ivan', 135, 344), ('olga', 136, 258), ('olga', 137, 935), ('artem', 145, 786), ('ivan', 146, 715), ('ivan', 149, 824), ('ivan', 149, 973), ('ivan', 151, 824), ('olga', 162, 679), ('ivan', 167, 308), ('olga', 169, 636), ('ivan', 180, 396), ('olga', 184, 256), ('olga', 189, 499), ('ivan', 193, 997), ('artem', 200, 671), ('artem', 200, 671), ('olga', 203, 470), ('olga', 204, 84), ('olga', 208, 81), ('ivan', 216, 143), ('ivan', 226, 666), ('olga', 240, 978), ('ivan', 247, 475), ('artem', 250, 461), ('olga', 251, 197), ('olga', 254, 426), ('ivan', 258, 621), ('olga', 263, 585), ('olga', 270, 294), ('olga', 273, 278), ('olga', 283, 609), ('olga', 287, 16), ('olga', 299, 360), ('olga', 300, 359), ('ivan', 304, 764), ('ivan', 304, 764), ('olga', 311, 713), ('olga', 314, 195), ('ivan', 319, 717), ('ivan', 349, 747), ('ivan', 351, 755), ('ivan', 381, 96), ('ivan', 381, 505), ('olga', 396, 145), ('ivan', 402, 401), ('artem', 402, 836), ('ivan', 423, 758), ('olga', 424, 585), ('olga', 434, 160), ('ivan', 435, 210), ('ivan', 435, 210), ('ivan', 436, 323), ('ivan', 449, 850), ('olga', 454, 431), ('ivan', 463, 316), ('olga', 473, 347), ('olga', 473, 347), ('ivan', 477, 352), ('ivan', 480, 428), ('ivan', 480, 585), ('olga', 486, 281), ('ivan', 505, 48), ('olga', 505, 613), ('olga', 514, 86), ('ivan', 518, 649), ('ivan', 558, 266), ('artem', 570, 732), ('ivan', 571, 873), ('olga', 577, 857), ('ivan', 579, 33), ('ivan', 595, 754), ('olga', 598, 611), ('olga', 604, 309), ('olga', 614, 704), ('olga', 615, 951), ('ivan', 622, 525), ('olga', 623, 904), ('ivan', 631, 10), ('ivan', 636, 906), ('ivan', 639, 500), ('ivan', 647, 160), ('olga', 651, 529), ('olga', 674, 47), ('olga', 675, 525), ('olga', 676, 882), ('olga', 679, 98), ('olga', 702, 682), ('ivan', 713, 252), ('olga', 721, 503), ('ivan', 722, 720), ('artem', 724, 145), ('ivan', 737, 478), ('ivan', 746, 489), ('ivan', 756, 858), ('ivan', 758, 858), ('ivan', 760, 214), ('ivan', 767, 166), ('olga', 768, 984), ('ivan', 773, 227), ('olga', 778, 305), ('ivan', 780, 426), ('olga', 815, 11), ('ivan', 819, 627), ('olga', 838, 156), ('olga', 843, 177), ('ivan', 844, 317), ('ivan', 846, 264), ('olga', 855, 361), ('olga', 858, 287), ('olga', 862, 798), ('ivan', 868, 414), ('olga', 869, 364), ('ivan', 869, 415), ('ivan', 874, 529), ('olga', 875, 386), ('olga', 877, 788), ('ivan', 878, 619), ('ivan', 883, 409), ('olga', 886, 557), ('olga', 899, 993), ('ivan', 905, 436), ('ivan', 906, 435), ('olga', 906, 524), ('ivan', 917, 151), ('olga', 924, 148), ('olga', 926, 562), ('ivan', 940, 834), ('ivan', 947, 949), ('artem', 948, 310), ('olga', 949, 781), ('olga', 959, 843), ('ivan', 968, 453), ('ivan', 975, 821), ('artem', 979, 573), ('olga', 981, 619), ('ivan', 992, 121), ('artem', 996, 252)]

"""

board1 = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]


if __name__ == "__main__":
    # test_solution()
    test_solution_on_big_data()
