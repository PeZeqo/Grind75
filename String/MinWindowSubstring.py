"""
Solution:
Runtime 80% O(N)
Memory 30% O(N)

Attempt 1:
Runtime 30% O(N)
Memory 67% O(N)
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minWindow = math.inf
        winStart = 0

        need = defaultdict(int)
        for c in t:
            need[c] += 1

        cur = defaultdict(int)
        left = 0
        right = 0
        valid = 0
        while right < len(s):
            char = s[right]
            if char not in need:
                if left == right:
                    left += 1
                right += 1
                continue

            cur[char] += 1
            if cur[char] == need[char]:
                valid += 1

            while valid == len(need):
                curWindow = right - left + 1
                if curWindow < minWindow:
                    minWindow = curWindow
                    winStart = left

                remChar = s[left]
                if remChar in cur:
                    cur[remChar] -= 1
                    if cur[remChar] < need[remChar]:
                        valid -= 1
                left += 1
            right += 1

        return "" if minWindow == math.inf else s[winStart:winStart + minWindow]

    def minWindowAttempt1(self, s: str, t: str) -> str:
        minWindow = math.inf
        winStart = -1

        cur = defaultdict(int)
        for c in t:
            cur[c] += 1
        tCharSet = set(t)

        left = 0
        right = 0
        while right < len(s):
            char = s[right]
            if char not in tCharSet:
                if left == right:
                    left += 1
                right += 1
                continue

            cur[char] -= 1
            if cur[char] < 0:
                while True:
                    remChar = s[left]
                    if remChar in tCharSet:
                        if cur[remChar] >= 0:
                            break
                        cur[remChar] += 1
                    left += 1
            if all(v <= 0 for v in cur.values()):
                curWindow = right - left + 1
                if curWindow < minWindow:
                    minWindow = curWindow
                    winStart = left
            right += 1

        return "" if winStart == -1 else s[winStart:winStart + minWindow]
