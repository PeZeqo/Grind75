"""
Solution:
Runtime 93% O(N)
Memory 80% O(1)

Attempt 1:
Runtime 50% O(N)
Memory 13% O(1)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def preorder(node: Optional[TreeNode]) -> int:
            nonlocal res
            if node is None:
                return 0

            lM = preorder(node.left)
            if lM < 0:
                lM = 0

            rM = preorder(node.right)
            if rM < 0:
                rM = 0

            curMax = lM + rM + node.val
            if res < curMax:
                res = curMax
            return max(lM, rM) + node.val

        preorder(root)
        return res

    def maxPathSumAttempt1(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def preorder(node: Optional[TreeNode]) -> int:
            nonlocal res
            if node is None:
                return -math.inf, -math.inf
            lM, lBM = preorder(node.left)
            rM, rBM = preorder(node.right)
            curM = max(node.val + lM, node.val + rM, node.val)
            curBM = max(lBM, rBM, node.val + lM + rM, node.val)
            if res < curM:
                res = curM
            if res < curBM:
                res = curBM
            return curM, curBM

        preorder(root)
        return res
