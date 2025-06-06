"""
Solution:
Runtime 99% O(M * L) (Technically with our constraints this is O(M * 26[num chars] * 10[max word length]) -> O(M))
Memory 74% O(M * L)

Attempt2:
Runtime 57% O(M * L)
Memory 93% O(M * L) (store height as local int instead of in tuples in stack)

Attempt1:
Runtime 55% O(M * L)
Memory 58% O(M * L)
"""


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        wordSet.add(beginWord)
        if endWord not in wordSet:
            return 0

        beginSet = {beginWord}
        endSet = {endWord}
        word_len = len(beginWord)
        height = 1

        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            next_level = set()
            for word in beginSet:
                if word not in wordSet:
                    continue
                wordSet.remove(word)

                wrdList = list(word)
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        wrdList[i] = c
                        newWord = ''.join(wrdList)
                        if newWord in endSet:
                            return height + 1
                        if newWord in wordSet:
                            next_level.add(newWord)
                    wrdList[i] = word[i]

            beginSet = next_level
            height += 1

        return 0

    def ladderLengthAttempt2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        wordSet.add(beginWord)
        if endWord not in wordSet:
            return 0
        stack = deque([beginWord])

        height = 0
        while stack:
            height += 1
            for _ in range(len(stack)):
                word = stack.popleft()
                if word not in wordSet:
                    continue
                wordSet.remove(word)

                wrdList = list(word)
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        wrdList[i] = c
                        nxtWord = ''.join(wrdList)
                        if nxtWord in wordSet:
                            if nxtWord == endWord:
                                return height + 1
                            stack.append(nxtWord)
                    wrdList[i] = word[i]

        return 0

    def ladderLengthAttempt1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        wordList.add(beginWord)
        if endWord not in wordList:
            return 0
        stack = deque([(beginWord, 1)])

        while stack:
            word, count = stack.popleft()
            if word not in wordList:
                continue
            wordList.remove(word)
            if word == endWord:
                return count
            wrdList = list(word)
            for i in range(len(word)):
                for j in range(26):
                    wrdList[i] = chr(ord('a') + j)
                    nxtWord = ''.join(wrdList)
                    if nxtWord in wordList:
                        stack.append((nxtWord, count + 1))
                wrdList[i] = word[i]

        return 0
