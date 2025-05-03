"""
Runtime 81% O(m * n)
Memory 89% O(m * n)
"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()

        M = len(mat)
        N = len(mat[0])
        maxValue = M * N

        for m in range(M):
            for n in range(N):
                if mat[m][n] == 0:
                    queue.append((m, n))
                else:
                    mat[m][n] = maxValue

        while queue:
            m, n = queue.popleft()
            nextValue = mat[m][n] + 1

            toVisit = [(m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1)]
            for nextM, nextN in toVisit:
                if 0 <= nextM < M and 0 <= nextN < N and mat[nextM][nextN] > nextValue:
                    mat[nextM][nextN] = nextValue
                    queue.append((nextM, nextN))

        return mat
