"""
Runtime 35% O(n)
Memory 8% O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, -math.inf, math.inf)])

        while queue:
            node, lower, upper = queue.popleft()
            if node is None:
                continue
            if lower < node.val < upper:
                queue.append((node.left, lower, node.val))
                queue.append((node.right, node.val, upper))
            else:
                return False

        return True

