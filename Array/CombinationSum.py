"""
Runtime 90% O(n ^ (T / M)) (M == min(candidates) as this is the maximum recursion depth, each loop running at O(n))
Memory 40% O(n)
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def recur(value, ind, soFar):
            for nextInd in range(ind, -1, -1):
                nextCandidate = candidates[nextInd]
                soFar.append(nextCandidate)
                nextValue = value - nextCandidate
                if nextValue == 0:
                    res.append(soFar.copy())
                if nextValue > 0:
                    recur(nextValue, nextInd, soFar)
                soFar.pop()

        recur(target, len(candidates) - 1, [])
        return res
