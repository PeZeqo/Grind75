"""
Solution:
Runtime 75% O(N)
Memory 10% O(1)

Attempt 1:
Runtime -% O(N^2) (non-working solution)
Memory -% O(N)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
        return

    def rotateAttempt1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return

        def rotateOnce(start: int):
            loop = False
            i = start
            swap = (i + k) % len(nums)
            temp = nums[i]
            while i != start or not loop:
                loop = True
                temp, nums[swap] = nums[swap], temp
                i = (i + k) % len(nums)
                swap = (swap + k) % len(nums)

        if len(nums) % k == 0:
            for start in range(k):
                rotateOnce(start)
        else:
            rotateOnce(0)

        return
