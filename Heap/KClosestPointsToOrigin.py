import heapq

"""
Solution: 
Runtime 99% O(nlog(n))
Memory 93% O(n)

Attempt 1:
Runtime 41% O(nlog(n))
Memory 74% O(n)
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:k]

    def kClosestAttempt1(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for ind, point in enumerate(points):
            distance = -math.sqrt((point[0] ** 2) + (point[1] ** 2))
            if len(heap) >= k:
                heapq.heappushpop(heap, (distance, ind))
            else:
                heapq.heappush(heap, (distance, ind))

        return [points[heapq.heappop(heap)[1]] for _ in range(k)]
