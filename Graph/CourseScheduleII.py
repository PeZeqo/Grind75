"""
Solution:
Runtime 77% O(V + E)
Memory 60% O(V)
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for c, p in prerequisites:
            adjList[c].append(p)

        def topoSort(i, visited, adjList, stack):
            if visited[i] != 0:
                return visited[i] == 1
            visited[i] = -1
            for pre in adjList[i]:
                if not topoSort(pre, visited, adjList, stack):
                    return False
            stack.append(i)
            visited[i] = 1
            return True

        visited = [0] * numCourses
        stack = []
        for i in range(numCourses):
            if visited[i] == 0:
                if not topoSort(i, visited, adjList, stack):
                    return []

        return stack
