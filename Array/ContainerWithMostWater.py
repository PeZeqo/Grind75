"""
Solution:
Runtime 85% O(N)
Memory 24% O(1)
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        mostWater = 0

        while left < right:
            currWater = min(height[left], height[right]) * (right - left)
            if currWater > mostWater:
                mostWater = currWater

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return mostWater
