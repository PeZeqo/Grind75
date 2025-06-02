"""
Solution:
Runtime 80% O(N)
Memory 30% O(N)

Attempt 1:
Runtime 30% O(N)
Memory 67% O(N)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    nullChar = 'N'

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder(node: TreeNode):
            if node is None:
                res.append(self.nullChar)
                return

            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(','))

        def preorder():
            v = data.popleft()

            if v == self.nullChar:
                return None

            root = TreeNode(int(v))
            root.left = preorder()
            root.right = preorder()
            return root

        return preorder()


class CodecAttempt1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""
        s = deque([root])
        while s:
            node = s.popleft()
            if node is None:
                res += "N"
            else:
                res += str(node.val)
                s.append(node.left)
                s.append(node.right)
            res += ','
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def makeNode(ind: int):
            if ind >= len(data):
                return None, ind

            if data[ind] == "N":
                return None, ind + 1

            cur = ""
            while data[ind] != ',':
                cur += data[ind]
                ind += 1
            ind += 1
            return TreeNode(cur), ind

        if not data or data[0] == "N":
            return None
        head, ind = makeNode(0)
        s = deque([head])

        while s and ind < len(data):
            node = s.popleft()
            if node is None:
                continue
            node.left, ind = makeNode(ind)
            if node.left is not None:
                s.append(node.left)
            node.right, ind = makeNode(ind)
            if node.right is not None:
                s.append(node.right)

        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))