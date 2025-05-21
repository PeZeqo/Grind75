"""
Solution:
Runtime 45% O(N)
Memory 80% O(N)
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        pCharSet = set()
        chars = defaultdict(int)
        for char in p:
            chars[char] -= 1
            pCharSet.add(char)

        res = []
        for ind in range(len(s)):
            newChar = s[ind]
            chars[newChar] = chars.get(newChar, 0) + 1

            if ind >= len(p):
                remCharInd = ind - len(p)
                remChar = s[remCharInd]
                chars[remChar] = chars.get(remChar, 0) - 1

            if newChar in pCharSet and all([v == 0 for v in chars.values()]):
                res.append(ind - len(p) + 1)

        return res
