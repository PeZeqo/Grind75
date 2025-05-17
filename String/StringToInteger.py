"""
Solution:
Runtime 100% O(N) (num chars)
Memory 95% O(1)
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        is_negative = False
        if s[0] in {'-', '+'}:
            is_negative = True if s[0] == '-' else False
            s = s[1:]

        intLimit = (2 ** 31) if is_negative else (2 ** 31) - 1

        s.lstrip('0')
        num = 0
        for c in s:
            if not c.isnumeric():
                break

            num *= 10
            num += int(c)

            if num >= intLimit:
                num = intLimit
                break

        return -num if is_negative else num
