"""
Solution:
Runtime 83% O(NlogN)
Memory 17% O(N)

Attempt1:
Runtime 68% O(N^2)
Memory 54% O(N)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = []
        for num in nums:
            if not subsequence or num > subsequence[-1]:
                subsequence.append(num)
            else:
                repInd = bisect.bisect_left(subsequence, num)
                subsequence[repInd] = num

        return len(subsequence)

    def lengthOfLISAttempt1(self, nums: List[int]) -> int:
        mem = [1] * len(nums)

        for i, num in enumerate(nums):
            maxLis = 1
            for j in range(i - 1, -1, -1):
                if nums[j] < num and mem[j] >= maxLis:
                    maxLis = mem[j] + 1
            mem[i] = maxLis

        return max(mem)
