"""
Solution (Recursive):
Runtime 66% O(N)
Memory 61% O(N)

Attempt 1 (Recursive + List splicing):
Runtime 25% O(N^2)
Memory 42% O(N^2)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preToIn = {value: ind for ind, value in enumerate(inorder)}

        def rec(pL, pR, iL, iR):
            if pL > pR:
                return None

            nodeVal = preorder[pL]
            root = TreeNode(nodeVal)

            # Determine the size of the left subtree
            rootInd = preToIn[nodeVal]
            left_size = rootInd - iL

            root.left = rec(pL + 1, pL + left_size, iL, rootInd - 1)
            root.right = rec(pL + left_size + 1, pR, rootInd + 1, iR)

            return root

        return rec(0, len(preorder) - 1, 0, len(preorder) - 1)
