"""
Solution:
Runtime 92% O(4^N)
Memory 65% O(4^N)
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        queue = deque([""])
        numToChar = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

        for digit in digits:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for char in numToChar[digit]:
                    queue.append(cur + char)

        return list(queue)
