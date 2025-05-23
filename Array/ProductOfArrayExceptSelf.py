"""
Runtime 94% O(n)
Memory 93% O(1) (excluding output array)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        currMult = 1
        for i in range(len(nums)):
            ans[i] = currMult
            currMult *= nums[i]

        currMult = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= currMult
            currMult *= nums[i]

        return ans
