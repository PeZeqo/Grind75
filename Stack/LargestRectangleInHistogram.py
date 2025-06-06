"""
Solution:
Runtime 98% O(N)
Memory 82% O(N)

Attempt 1:
Runtime -% O(N^2)
Memory -% O(N^2) (memory limit exceeded)
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                curMax = width * height
                if curMax > maxArea:
                    maxArea = curMax
            stack.append(i)

        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            curMax = width * height
            if curMax > maxArea:
                maxArea = curMax

        return maxArea

    def largestRectangleAreaAttempt1(self, heights: List[int]) -> int:
        seen = set()
        largest = 0

        def searchAround(ind: int):
            nonlocal seen
            nonlocal largest

            left = ind
            right = left
            curMin = math.inf
            H = len(heights)

            while left >= 0 and right < H:
                if (left, right) in seen:
                    break
                seen.add((left, right))
                lH = heights[left]
                rH = heights[right]
                curMin = min(curMin, lH, rH)
                curLargest = curMin * (right - left + 1)
                largest = max(largest, curLargest)
                if (curMin * H) <= largest:
                    break
                nL = -math.inf if left <= 0 else heights[left - 1]
                nR = -math.inf if right >= (H - 1) else heights[left + 1]
                if nL >= nR:
                    left -= 1
                else:
                    right += 1

        for i in range(len(heights)):
            searchAround(i)

        return largest
