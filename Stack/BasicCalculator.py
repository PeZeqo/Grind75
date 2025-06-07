"""
Solution:
Runtime 74% O(N)
Memory 35% O(N)

Attempt1:
Runtime 16% O(N) (lots of reprocessing of characters)
Memory 92% O(N)
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        res = 0
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num *= 10
                num += int(char)
            elif char in '+-':
                res += num * sign
                num = 0
                sign = -1 if char == '-' else 1
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
                sign = 1

        return res + num * sign

    def calculateAttemp1(self, s: str) -> int:
        def operate(stack: list):
            if len(stack) <= 1 or stack[-2] not in {'-', '+'}:
                return
            res = stack.pop()
            operation = stack.pop()
            if stack and isinstance(stack[-1], int):
                num2 = stack.pop()
                res = num2 + res if operation == '+' else num2 - res
            else:
                res = -res
            stack.append(res)

        s = s.replace(' ', '')
        stack = []
        numeric = set('0123456789')
        operation = set('+-')
        i = 0
        while i < len(s):
            char = s[i]
            if char in numeric:
                num = 0
                while i < len(s) and s[i] in numeric:
                    num *= 10
                    num += int(s[i])
                    i += 1
                stack.append(num)
                operate(stack)
            elif char in operation:
                stack.append(char)
                i += 1
            else:
                if char == ')':
                    operate(stack)
                    # remove leading parenthesis
                    num = stack.pop()
                    stack.pop()
                    stack.append(num)
                    operate(stack)
                else:
                    stack.append(char)
                i += 1

        while len(stack) > 1:
            operate(stack)
        return stack[0]
