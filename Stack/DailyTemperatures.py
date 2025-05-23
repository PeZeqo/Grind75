"""
Solution:
Runtime 82% O(N)
Memory 95% O(N)

Attempt 1:
Runtime 35% O(N)
Memory 27% O(N)

Attempt 2:
Runtime 5% O(Nlog(n))
Memory 27% O(N)
"""

import heapq


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for ind, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                pastInd = stack.pop()
                res[pastInd] = ind - pastInd
            stack.append(ind)

        return res

    def dailyTemperaturesAttempt2(self, temperatures: List[int]) -> List[int]:
        # creates tuples, let's try to avoid this
        stack = []
        res = [0] * len(temperatures)
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, pastInd = stack.pop()
                res[pastInd] = ind - pastInd
            stack.append((temp, ind))

        return res

    def dailyTemperaturesAttempt1(self, temperatures: List[int]) -> List[int]:
        # this solution is only okay if inplace modification is acceptable to avoid additional memory for result array
        heap = []
        for ind, temp in enumerate(temperatures):
            while heap and heap[0][0] < temp:
                _, pastInd = heapq.heappop(heap)
                temperatures[pastInd] = ind - pastInd
            heapq.heappush(heap, (temp, ind))

        while heap:
            temperatures[heapq.heappop(heap)[1]] = 0

        return temperatures
