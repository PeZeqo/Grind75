"""
Solution:
Runtime 100% O(N)
Memory 27% O(1)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0

        def inorder(node):
            if node.left and (res := inorder(node.left)) is not None:
                return res

            self.i += 1
            if self.i == k:
                return node.val

            if node.right:
                return inorder(node.right)
            return None

        return inorder(root)
