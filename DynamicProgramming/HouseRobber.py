"""
Solution:
Runtime 100% O(N)
Memory 34% O(1)

Attempt 1:
Runtime 100% O(N)
Memory 30% O(N)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # minimize memory usage since we only need to know values of skipping last house or robbing it
        maxRobLeft = [0] * 3

        for ind, amount in enumerate(nums):
            maxIfSkip = maxRobLeft[1]
            maxIfRob = amount + maxRobLeft[0]
            maxRobLeft[2] = max(maxIfSkip, maxIfRob)

            # shift over memory of amounts to block next house from robbing this house
            maxRobLeft[0] = maxRobLeft[1]
            maxRobLeft[1] = maxRobLeft[2]

        return maxRobLeft[-1]

    def robAttempt1(self, nums: List[int]) -> int:
        maxRobLeft = [0] * len(nums)

        for ind, amount in enumerate(nums):
            if ind > 0:
                maxIfSkip = maxRobLeft[ind - 1]
            else:
                maxIfSkip = 0

            if ind > 1:
                maxIfRob = amount + maxRobLeft[ind - 2]
            else:
                maxIfRob = amount

            maxRobLeft[ind] = max(maxIfSkip, maxIfRob)

        return maxRobLeft[-1]
