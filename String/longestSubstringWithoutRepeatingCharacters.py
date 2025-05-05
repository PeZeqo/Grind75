"""
Solution:
Runtime 56% O(n)
Memory 12% O(n)

Attempt 1:
Runtime 68% O(n)
Memory 12% O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsToInd = {}
        maxLen = 0
        startInd = 0

        for endInd, char in enumerate(s):
            if char in charsToInd:
                startInd = max(startInd, charsToInd[char] + 1)
            charsToInd[char] = endInd

            maxLen = max(maxLen, endInd - startInd + 1)

        return maxLen

    def lengthOfLongestSubstringAttempt1(self, s: str) -> int:
        charsInString = set()
        maxLen = 0
        startInd = 0
        endInd = 0

        while endInd < len(s):
            char = s[endInd]
            while char in charsInString:
                charsInString.remove(s[startInd])
                startInd += 1
            charsInString.add(char)

            maxLen = max(maxLen, endInd - startInd + 1)
            endInd += 1

        return maxLen
