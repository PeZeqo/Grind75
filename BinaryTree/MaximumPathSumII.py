"""
Solution:
Runtime 100% O(N)
Memory 41% O(H) (maximum height of tree)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node: Optional[TreeNode], path: List[int], curSum: int):
            if node.left is None and node.right is None:
                if curSum + node.val == targetSum:
                    nonlocal res
                    res.append(path + [node.val])

            curSum += node.val
            path.append(node.val)
            if node.left is not None:
                dfs(node.left, path, curSum)
            if node.right is not None:
                dfs(node.right, path, curSum)
            path.pop()

        if root is not None:
            dfs(root, [], 0)
        return res
