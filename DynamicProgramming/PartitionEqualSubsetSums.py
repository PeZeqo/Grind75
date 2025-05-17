"""
Solution:
Runtime 95% O(~N^2) (N * 2^N worst case)
Memory 60% O(2^N (worst case: powerset)

Attempt 1:
Runtime 89% O(~N^2) (N * 2^N worst case)
Memory 59% O(2^N) (worst case: powerset)
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        seen = set([0])

        for num in nums:
            seen.update([v + num for v in seen if v + num <= target])
            if target in seen:
                return True

        return False

    def canPartitionAttempt1(self, nums: List[int]) -> bool:
        seen = set([0])
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        for num in nums:
            for other in list(seen):
                if (other + total) < target:
                    continue

                value = num + other
                if value == target:
                    return True
                seen.add(value)
            total -= num

        return False
