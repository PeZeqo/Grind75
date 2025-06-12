"""
Solution:
Runtime 99% O(N)
Memory 89% O(N)
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        while nums:
            num = nums.pop()
            low = num - 1
            high = num + 1
            count = 1

            while low in nums:
                count += 1
                nums.remove(low)
                low -= 1

            while high in nums:
                count += 1
                nums.remove(high)
                high += 1

            if count > longest:
                longest = count

        return longest
