"""
Runtime 100% O(n * n!)
Memory 33% O(n * n!)
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = deque([[nums[0]]])

        for num in nums[1:]:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for i in range(len(cur) + 1):
                    queue.append(cur[:i] + [num] + cur[i:])

        return list(queue)
