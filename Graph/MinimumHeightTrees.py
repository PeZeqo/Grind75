"""
Solution:
Runtime 81% O(N)
Memory 75% O(N)
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        adj = defaultdict(list)
        degree = [0 for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
            degree[x] += 1
            degree[y] += 1

        leaves = deque([ind for ind, value in enumerate(degree) if value == 1])
        nodesLeft = n

        while nodesLeft > 2:
            numLeaves = len(leaves)
            nodesLeft -= numLeaves
            for _ in range(numLeaves):
                leaf = leaves.popleft()
                for x in adj[leaf]:
                    degree[x] -= 1
                    if degree[x] == 1:
                        leaves.append(x)

        return list(leaves)
