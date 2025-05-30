"""
Solution:
Runtime 98% O(N)
Memory 80% O(N)
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        numNegs = sum(1 for n in nums if n < 0)

        for numList in [nums, reversed(nums)]:
            subProd = 1
            curNegs = numNegs
            for num in numList:
                subProd *= num
                if num < 0:
                    curNegs -= 1

                if subProd > maxProd:
                    maxProd = subProd

                if (subProd < 0 and curNegs == 0) or subProd == 0:
                    subProd = 1

        return maxProd
