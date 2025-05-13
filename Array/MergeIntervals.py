"""
Runtime 100% O(n)
Memory 63% O(n)
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []

        cur = intervals[0]
        for interval in intervals[1:]:
            if cur[1] >= interval[0]:
                cur[1] = max(cur[1], interval[1])
            else:
                res.append(cur)
                cur = interval
        res.append(cur)

        return res
