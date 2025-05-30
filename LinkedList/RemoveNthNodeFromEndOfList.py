"""
Solution:
Runtime 100% O(N)
Memory 54% O(1)

Attempt 1:
Runtime 100% O(N)
Memory 54% O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        slow = None
        fast = head
        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        slow = head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        remNode = slow.next
        slow.next = remNode.next
        del remNode

        return head

    def removeNthFromEndAttempt1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        numNodes = 0
        node = head
        while node is not None:
            numNodes += 1
            node = node.next

        if n == numNodes:
            return head.next

        remNode = numNodes - n
        cur = 1
        node = head
        while cur != remNode:
            node = node.next
            cur += 1

        remNode = node.next
        node.next = remNode.next if remNode is not None else None
        del remNode

        return head
