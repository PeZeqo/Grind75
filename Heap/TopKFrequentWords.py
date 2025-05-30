"""
Solution:
Runtime 100% O(Nlog(k))
Memory 88% O(N)
"""

import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = defaultdict(int)
        for word in words:
            wordCount[word] += 1

        heap = [(-count, word) for word, count in wordCount.items()]
        heapq.heapify(heap)

        """
        This is O(nlog(n)) while making a heap from list is O(n)
        heap = []
        for word, count in wordCount.items():
            heapq.heappush(heap, (-count, word))
        """
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
