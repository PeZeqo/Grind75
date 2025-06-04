"""
Solution:
Runtime 90% O(Nlog(N)) (N = total number of ListNodes across lists)
Memory 54% O(N)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        for i in range(len(lists)):
            node = lists[i]
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))

        head = ListNode()
        node = head
        while heap:
            _, i, nextNode = heapq.heappop(heap)
            node.next = nextNode
            node = node.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return head.next
