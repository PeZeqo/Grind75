"""
Solution (DFS):
Runtime 100% O(N)
Memory 60% O(H) (height of tree)

Attempt 1 (BFS):
Runtime 100% O(N)
Memory 36% O(W) (maximum width of tree, worst case N/2, so ~= O(N))
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node=root, level=1):
            if not node:
                return
            if level > len(res):
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs()
        return res

    def rightSideViewAttempt1(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []

        while queue:
            valueFound = False
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue

                if not valueFound:
                    res.append(node.val)
                    valueFound = True

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return res
