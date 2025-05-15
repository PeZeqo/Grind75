"""
Solution (DP):
Runtime 70% O(n^2)
Memory 93% O(n)

Attempt 2 (DFS):
Runtime 70% O(n^2) (checking all substrings potentially)
Memory 74% O(n^2) (storing all substrings potentially)

Attempt 1 (BFS):
Runtime -% O(n^2) (checking all substrings potentially)
Memory -% O(2^n) (memory exceeded error, not tracking visited will blow up queue size with BFS)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dpMem = [False] * (n + 1)
        # empty string is valid solution
        dpMem[0] = True

        # tracking shortest word let's us avoid looping over values of (I, J) that would produce a substring too short to exist in wordDict
        shortestWord = min([len(word) for word in wordDict])

        # use a set for constant time hashed lookups
        wordDict = set(wordDict)

        for i in range(shortestWord, n + 1):
            for j in range(i - shortestWord + 1):
                if dpMem[j] and s[j:i] in wordDict:
                    dpMem[i] = True
                    break

        return dpMem[-1]

    def wordBreakAttmpt2(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        shortestWord = min([len(word) for word in wordDict])

        stack = [s]
        visited = set()

        while stack:
            word = stack.pop()
            if word in visited or len(word) < shortestWord:
                continue
            if word in wordDict:
                return True
            visited.add(word)

            nextWord = ""
            for ind, char in enumerate(word):
                nextWord += char
                if nextWord in wordDict:
                    stack.append(word[ind + 1:])

        return False

    def wordBreakAttmpt1(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        queue = deque([s])

        while queue:
            word = queue.popleft()
            if word in wordDict:
                return True

            nextWord = ""
            for ind, char in enumerate(word):
                nextWord += char
                if nextWord in wordDict:
                    queue.append(word[ind + 1:])

        return False
