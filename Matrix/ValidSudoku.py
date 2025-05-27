"""
Solution:
Runtime 100% O(M * N)
Memory 44% O(M * N)

Attempt 1:
Runtime -% O(M * N)
Memory -% O(M * N)
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for m in range(len(board)):
            for n in range(len(board)):
                char = board[m][n]
                if char == '.':
                    continue
                for variation in [(0, m, char), (1, n, char), (2, m // 3, n // 3, char)]:
                    if variation in s:
                        return False
                    s.add(variation)

        return True

    def isValidSudokuAttempt1(self, board: List[List[str]]) -> bool:
        for m in range(len(board)):
            s = set()
            for n in range(len(board)):
                char = board[m][n]
                if char != '.' and char in s:
                    return False
                s.add(char)

        for n in range(len(board)):
            s = set()
            for m in range(len(board)):
                char = board[m][n]
                if char != '.' and char in s:
                    return False
                s.add(char)

        # compare squares

        return True
