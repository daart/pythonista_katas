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


def search(grid, word, index, row, col):
    # if we are out of boundary OR if current grid_char doesn't equal to current word_char
    if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] != word[index]:
        return False
    # if we are at the end of the target word
    if index == len(word) - 1:
        return True

    current_char = grid[row][col]
    grid[row][col] = '!'  # mark already visited cell
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
    >>> main([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")
    True
    """

    for r in range(len(board)):
        for c in range(len(board[0])):
            if word[0] == board[r][c] and search(board, word, 0, r, c):
                return True

    return False


board1 = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
