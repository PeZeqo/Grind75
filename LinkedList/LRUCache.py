"""
Solution:
Runtime 59% O(1)
Memory 46% O(N)
"""


class Node:

    def __init__(self, value: int = None, prev: 'Node' = None, next: 'Node' = None):
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.nodeToKey = {}
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def _bump_node(self, node: Node):
        # if node exists, remove from current place
        if node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev

        # make node first in linked list
        node.prev = self.head
        nextNode = self.head.next
        self.head.next = node
        node.next = nextNode
        nextNode.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._bump_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
        else:
            node = Node(value)
            self.nodeToKey[node] = key
        self.cache[key] = node
        self._bump_node(node)

        # evict last node in linked list if over capacity in cache
        if len(self.cache) > self.capacity:
            remNode = self.tail.prev
            del self.cache[self.nodeToKey[remNode]]
            del self.nodeToKey[remNode]
            prevRem = remNode.prev
            self.tail.prev = prevRem
            prevRem.next = self.tail
            del remNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
