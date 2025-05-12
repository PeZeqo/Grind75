"""
Runtime 100% O(log(N)))
Memory 22% O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            cur = nums[mid]
            curR = nums[right]

            if cur == target:
                return mid
            elif (
                    (cur < target and (target <= curR or cur > curR)) or
                    (cur > curR and target <= curR)
            ):
                left = mid + 1
            else:
                right = mid - 1

        return -1
