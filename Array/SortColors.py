"""
Runtime 100% O(n)
Memory 33% O(1)
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colorInd = [0, 0, 0]

        for ind, num in enumerate(nums):
            # swap numbers at correct index for color and the current index
            indexToInsertColor = colorInd[num]
            swap = nums[indexToInsertColor]
            nums[ind], nums[indexToInsertColor] = swap, num

            # if swapping a one, swap it again to be before all of the 2's
            if swap == 1:
                nums[colorInd[1]], nums[colorInd[2]] = nums[colorInd[2]], nums[colorInd[1]]

            for i in range(num, 3):
                colorInd[i] += 1

        return None
