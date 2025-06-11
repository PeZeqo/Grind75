"""
Solution:
Runtime 100% O(N)
Memory 83% O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        res = head.next
        prev = ListNode()

        while head and head.next:
            prev.next = head.next
            nxt = head.next
            head.next = nxt.next
            nxt.next = head
            prev = head
            head = head.next

        return res
