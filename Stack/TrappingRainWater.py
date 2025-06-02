"""
Solution:
Runtime 97% O(N)
Memory 20% O(1)

Attempt 1:
Runtime 5% O(N^2)
Memory 69% O(N)
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        maxL = height[left]
        right = len(height) - 1
        maxR = height[right]

        while left <= right:
            if maxL <= maxR:
                if height[left] > maxL:
                    maxL = height[left]
                res += maxL - height[left]
                left += 1
            else:
                if height[right] > maxR:
                    maxR = height[right]
                res += maxR - height[right]
                right -= 1

        return res

    def trapAttempt1(self, height: List[int]) -> int:
        amountRainCanHold = [0] * len(height)
        maxRain = 0
        left = 0
        right = len(height) - 1

        while left < right:
            lH = height[left]
            rH = height[right]
            rainAmount = min(lH, rH)
            if rainAmount > maxRain:
                maxRain = rainAmount
                for i in range(left + 1, right):
                    amountRainCanHold[i] = maxRain
            if lH <= rH:
                left += 1
            else:
                right -= 1

        return sum(max(0, amountRainCanHold[i] - height[i]) for i in range(len(height)))
