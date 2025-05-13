"""
Runtime 79% O(n)
Memory 10% O(1)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def checkAncestor(node: 'TreeNode'):
            if node is None:
                return None, False, False

            left, lP, lQ = checkAncestor(node.left)
            if lP and lQ:
                return left, lP, lQ

            right, rP, rQ = checkAncestor(node.right)
            if rP and rQ:
                return right, rP, rQ

            P = lP or rP or node is p
            Q = lQ or rQ or node is q
            return node, P, Q

        return checkAncestor(root)[0]
