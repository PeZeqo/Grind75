"""
Solution:
Runtime 100% O(N)
Memory 56% O(1)
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        swap = False
        for swapInd in range(len(nums) - 2, -1, -1):
            if nums[swapInd] < nums[swapInd + 1]:
                swap = True
                break

        if swap:
            minInd = swapInd + 1
            for i in range(minInd, len(nums)):
                if nums[swapInd] < nums[i] <= nums[minInd]:
                    minInd = i
            nums[swapInd], nums[minInd] = nums[minInd], nums[swapInd]
            swapInd += 1

        swapEnd = len(nums) - 1
        while swapInd < swapEnd:
            nums[swapInd], nums[swapEnd] = nums[swapEnd], nums[swapInd]
            swapInd += 1
            swapEnd -= 1

        return
