"""
Solution:
Runtime 95% O(L) (max length of word)
Memory 85% O(N * L)  (number of words in trie * max length of word)
"""


class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['*'] = {}

    def search(self, word: str) -> bool:
        # DFS approach to finding a match for words to account for wildcard
        stack = [(self.trie, 0)]
        while stack:
            trie, i = stack.pop()
            if i == len(word):
                if '*' in trie:
                    return True
                continue
            if word[i] == '.':
                for k, v in trie.items():
                    if k == '*':
                        continue
                    stack.append((v, i + 1))
            elif word[i] in trie:
                stack.append((trie[word[i]], i + 1))

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
