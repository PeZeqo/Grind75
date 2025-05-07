"""
Solution:
Runtime 65% O(N)
Memory 52% O(N)
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operations = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operations:
                v2 = s.pop()
                v1 = s.pop()
                if token == '+':
                    value = v1 + v2
                elif token == '-':
                    value = v1 - v2
                elif token == '*':
                    value = v1 * v2
                else:
                    value = int(v1 / v2)
                s.append(int(value))
            else:
                s.append(int(token))

        return s[0]
