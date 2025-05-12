"""
Runtime 77% O(M * N)
Memory 58% O(min(M, N)) (holds at most one diagnol set of nodes bound by this size)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        numIslands = 0

        def bfsVisit(m, n):
            queue = deque([(m, n)])

            while queue:
                m, n = queue.popleft()
                if grid[m][n] == '0':
                    continue

                grid[m][n] = '0'
                if 0 < m:
                    queue.append((m - 1, n))
                if 0 < n:
                    queue.append((m, n - 1))
                if m < M - 1:
                    queue.append((m + 1, n))
                if n < N - 1:
                    queue.append((m, n + 1))

        for m in range(M):
            for n in range(N):
                if grid[m][n] == '1':
                    numIslands += 1
                    bfsVisit(m, n)

        return numIslands
