"""
Solution:
Runtime 100% O(M*N)
Memory 88% O(M*N)
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(incValue: int, s: list):
            seen = set()
            while s:
                height, m, n = s.pop()
                if not (0 <= m < M and 0 <= n < N):
                    continue
                if (height, m, n) in seen or grid[m][n] >= incValue:
                    continue

                seen.add((height, m, n))
                curHeight = heights[m][n]
                if height <= curHeight:
                    grid[m][n] += incValue
                    s.extend(
                        [(curHeight, m + 1, n), (curHeight, m - 1, n), (curHeight, m, n + 1), (curHeight, m, n - 1)])

        s = []
        M = len(heights)
        N = len(heights[0])
        grid = [[0] * N for _ in range(M)]

        for m in range(M):
            s.append((0, m, 0))

        for n in range(N):
            s.append((0, 0, n))
        dfs(1, s)

        for m in range(M):
            s.append((0, m, N - 1))

        for n in range(N):
            s.append((0, M - 1, n))
        dfs(2, s)

        res = []
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 3:
                    res.append([m, n])
        return res
