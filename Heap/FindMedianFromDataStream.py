"""
Solution:
Runtime 55% O(Nlog(N))
Memory 13% O(N)
"""


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if (not self.minHeap and not self.maxHeap) or num < -self.minHeap[0]:
            heapq.heappush(self.minHeap, -num)
            if len(self.minHeap) >= (len(self.maxHeap) + 2):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        else:
            heapq.heappush(self.maxHeap, num)
            if len(self.maxHeap) >= (len(self.minHeap) + 2):
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        elif len(self.minHeap) == len(self.maxHeap):
            return (-self.minHeap[0] + self.maxHeap[0]) / 2.0
        else:
            return self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()