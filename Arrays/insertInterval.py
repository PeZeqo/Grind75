"""
Runtime 65% O(n)
Memory 20% O(n)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        lenIntervals = len(intervals)

        while i < lenIntervals and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        newInterval = [newInterval[0], newInterval[1]]
        while i < lenIntervals and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < lenIntervals:
            res.append(intervals[i])
            i += 1

        return res

    # def insertAttempt2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     res = []
    #     startInd = None
    #     startVal = newInterval[0]
    #     endInd = None
    #     endVal = newInterval[1]

    #     for ind, interval in enumerate(intervals):
    #         if newInterval[0] < interval[1]:
    #             startInd = ind
    #             startVal = min(interval[0], startVal)
    #             break
    #         else:
    #             res.append(interval)

    #     if startInd is None:
    #         res.append(newInterval)
    #         return res

    #     endInd = None
    #     for ind, interval in enumerate(intervals[startInd:]):
    #         ind = ind + startInd
    #         if newInterval[1] < interval[0]:
    #             if ind > 0:
    #                 endVal = max(intervals[ind-1][1], endVal)
    #             endInd = ind
    #             break

    #     # print(startVal, endVal, startInd, endInd)
    #     # print(res)
    #     if not endInd:
    #         endVal = max(endVal, intervals[-1][1])
    #     res.append([startVal, endVal])
    #     # print(res)
    #     if endInd:
    #         res.extend(intervals[endInd:])
    #     # print(res)
    #     return res

    # def insertAttempt1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     res = []
    #     startInd = None
    #     startVal = newInterval[0]

    #     for ind, interval in enumerate(intervals):
    #         if interval[0] <= newInterval[0] and interval[1] >= newInterval[0]:
    #             startInd = ind
    #             startVal = min(interval[0], startVal)
    #             break

    #     if startInd is None:
    #         intervals.append(newInterval)
    #         return intervals

    #     endInd = startInd
    #     endVal = newInterval[1]

    #     for ind, interval in enumerate(intervals[startInd:]):
    #         if interval[0] <= newInterval[1] and interval[1] >= newInterval[1]:
    #             endInd = ind
    #             endVal = max(interval[1], endVal)
    #             break

    #     res = [interval for interval in intervals[:startInd]]
    #     res.append([startVal, endVal])
    #     if endInd:
    #         res.extend([interval for interval in intervals[endInd+1:]])
    #     return res
