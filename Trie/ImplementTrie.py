"""
Solution:
Runtime 97% O(N)
Memory 85% O(T) (characters seen)
"""


class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for char in word:
            trie[char] = trie.get(char, {})
            trie = trie[char]
        # use a '*' to indicate a word end
        trie['*'] = {}

    def search(self, word: str) -> bool:
        trie = self.trie
        for char in word:
            trie = trie.get(char, {})
        return '*' in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for char in prefix:
            trie = trie.get(char, {})
        return bool(trie)
