"""
Solution:
Runtime 92% O(M * N * 4^L) (4^L comes from branching factor of 4 axis to check by length of word)
Memory 65% O(L) (length of word)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])

        def dfs(m, n, ind):
            if 0 <= m < M and 0 <= n < N and board[m][n] == word[ind]:
                if ind == len(word) - 1:
                    return True
                char, board[m][n] = board[m][n], False
                for nextM, nextN in ((m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1)):
                    if dfs(nextM, nextN, ind + 1):
                        return True
                board[m][n] = char
            return False

        count = {}
        for m in range(M):
            for n in range(N):
                c = board[m][n]
                count[c] = count.get(c, 0) + 1

        if any([char not in count for char in word]):
            return False

        if count[word[0]] < count[word[-1]]:
            word = word[::-1]

        for m in range(M):
            for n in range(N):
                if dfs(m, n, 0):
                    return True

        return False
