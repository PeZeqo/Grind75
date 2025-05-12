"""
Runtime 100% O(M * N)
Memory 71% O(M * N) (worst case when all rotten to start)
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        queue = deque()
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 2:
                    queue.append((m, n))

        turns = -1

        while queue:
            rotted = False
            for _ in range(len(queue)):
                m, n = queue.popleft()
                if grid[m][n] == 0:
                    continue

                rotted = True
                grid[m][n] = 0
                if 0 < m:
                    queue.append((m - 1, n))
                if 0 < n:
                    queue.append((m, n - 1))
                if m < M - 1:
                    queue.append((m + 1, n))
                if n < N - 1:
                    queue.append((m, n + 1))
            if rotted:
                turns += 1

        for m in range(M):
            for n in range(N):
                nodeValue = grid[m][n]
                if nodeValue == 1:
                    return -1

        return max(0, turns)
