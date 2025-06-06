"""
Solution:
Runtime 85% O(NlogN)
Memory 84% O(N) (no heap overhead, just dp mem list)

Attempt2:
Runtime 87% O(NlogN)
Memory 46% O(N)

Attempt1:
Runtime -% O(N^2)
Memory -% O(E) (maximum endtime... memory limit exceeded)
"""


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        startTime.sort()

        dp = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            j = bisect.bisect_left(startTime, jobs[i][1])
            dp[i] = max(dp[i + 1], dp[j] + jobs[i][2])
        return dp[0]

    def jobSchedulingAttempt2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        heap = []
        curProf = 0
        maxProf = 0
        startToInd = [(s, i) for i, s in enumerate(startTime)]
        startToInd.sort()
        for start, i in startToInd:
            end = endTime[i]
            while heap and start >= heap[0][0]:
                nxtProf = -heapq.heappop(heap)[1]
                if nxtProf > curProf:
                    curProf = nxtProf
            newProf = curProf + profit[i]
            heapq.heappush(heap, (end, -newProf))
            if newProf > maxProf:
                maxProf = newProf

        return maxProf

    def jobSchedulingAttempt1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        maxProfit = [0] * max(endTime)
        for i in range(len(startTime)):
            start = startTime[i] - 1
            end = endTime[i] - 1
            curProfit = maxProfit[start] + profit[i]
            for j in range(end, len(maxProfit)):
                if curProfit <= maxProfit[j]:
                    break
                maxProfit[j] = curProfit

        return maxProfit[-1]
