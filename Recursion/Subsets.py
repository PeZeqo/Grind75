"""
Solution (DP):
Runtime 100% O(N * 2^N)
Memory 21% O(2^N)

Attempt 2 (Bit Trick + Bit Shift):
Runtime 100% O(N * 2^N) (slighly faster mathamatical operations)
Memory 24% O(2^N)

Attempt 1 (Bit Trick):
Runtime 100% O(N * 2^N)
Memory 21% O(2^N)
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [curr + [num] for curr in res]

        return res

    def subsetsAttempt2(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []

        for i in range(1 << N):
            row = []
            for j in range(N):
                if i & (1 << j):
                    row.append(nums[j])
            res.append(row)

        return res

    def subsetsAttempt1(self, nums: List[int]) -> List[List[int]]:
        res = [[] for _ in range(2 ** len(nums))]

        for ind, num in enumerate(nums):
            skip = (2 ** (ind + 1))
            for i in range(len(res)):
                if i % skip >= (skip // 2):
                    res[i].append(num)

        return res
