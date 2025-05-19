"""
Solution:
Runtime 100% O(N)
Memory 88% O(N) (reduced table)

Attempt 1:
Runtime 100% O(N)
Memory 61% O(N^2) (full m x n map)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maxDim = max(m, n)
        paths = [[0] * maxDim] * 2
        queue = deque([0])

        while queue:
            for _ in range(len(queue)):
                x = queue.popleft()

                if x >= maxDim or paths[1][x] != 0:
                    continue

                up = max(1, paths[0][x])
                left = max(1, paths[0][x - 1]) if x > 0 else 0
                paths[1][x] = up + left

                queue.extend([x, x + 1])

            for i in range(n):
                paths[0][i] = paths[1][i]
                paths[1][i] = 0

        return paths[0][0]

    def uniquePathsAttempt1(self, m: int, n: int) -> int:
        paths = [[1] * n] * m
        queue = deque([(0, 0)])

        while queue:
            x, y = queue.popleft()

            if x >= m or y >= n:
                continue

            up = 1 if x <= 0 else paths[x - 1][y]
            left = 1 if y <= 0 else path[x][y - 1]
            paths[x][y] = up + left

            queue.extend([(x + 1, y), (x, y + 1)])

        return paths[-1][-1]
