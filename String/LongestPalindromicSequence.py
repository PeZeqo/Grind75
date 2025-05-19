"""
Solution:
Runtime 71% O(N^2)
Memory 96% O(N)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = ""

        def checkPalindrome(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            return (right - left) + 1, left, right

        for i in range(len(s)):
            oddLen, oddL, oddR = checkPalindrome(i, i)
            evenLen, evenL, evenR = checkPalindrome(i, i + 1)

            if oddLen > longest:
                longest = oddLen
                res = s[oddL:oddR + 1]

            if evenLen > longest:
                longest = evenLen
                res = s[evenL:evenR + 1]

        return res
