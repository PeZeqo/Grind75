"""
Runtime 60% O(n)
Memory 41% O(1)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subSum = 0
        maxSubArray = nums[0]

        for num in nums:
            subSum += num
            maxSubArray = max(maxSubArray, subSum)
            if subSum < 0:
                subSum = 0

        return maxSubArray
