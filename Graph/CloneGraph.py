"""
Solution:
Runtime 31% O(V + E)
Memory 82% O(V)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        root = node
        nodes = {}
        queue = deque([node])

        while queue:
            node = queue.popleft()
            nodeCopy = nodes.get(node.val, Node(node.val))
            nodes[nodeCopy.val] = nodeCopy

            if not nodeCopy.neighbors:
                for neighbor in node.neighbors:
                    neighborNode = nodes.get(neighbor.val, Node(neighbor.val))
                    nodes[neighborNode.val] = neighborNode
                    nodeCopy.neighbors.append(neighborNode)
                    queue.append(neighbor)

        return nodes[root.val]
