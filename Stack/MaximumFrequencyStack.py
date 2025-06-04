"""
Solution:
Runtime 95% O(N)
Memory 21% O(N)

Attempt 2:
Runtime 26% O(Nlog(N))
Memory 81% O(N)

Attempt 1:
Runtime 5% O(N^2)
Memory 99% O(N)
"""


class FreqStack:

    def __init__(self):
        self.counts = defaultdict(int)
        self.stacks = defaultdict(list)
        self.curMax = 0

    def push(self, val: int) -> None:
        self.counts[val] += 1
        count = self.counts[val]
        if count > self.curMax:
            self.curMax = count
        self.stacks[count].append(val)

    def pop(self) -> int:
        val = self.stacks[self.curMax].pop()
        self.counts[val] -= 1
        if not self.stacks[self.curMax]:
            self.curMax -= 1
        return val


class FreqStackAttempt2:

    def __init__(self):
        self.inc = 0
        self.heap = []
        self.d = defaultdict(int)

    def push(self, val: int) -> None:
        self.d[val] += 1
        heapq.heappush(self.heap, (-self.d[val], -self.inc, val))
        self.inc += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.d[val] -= 1
        return val


class FreqStackAttempt1:

    def __init__(self):
        self.s = []
        self.d = defaultdict(int)
        self.curMax = 0

    def push(self, val: int) -> None:
        self.s.append(val)
        self.d[val] += 1
        if self.d[val] > self.curMax:
            self.curMax = self.d[val]

    def pop(self) -> int:
        for i, val in enumerate(reversed(self.s)):
            if self.d[val] == self.curMax:
                self.s.pop(-(i + 1))
                self.d[val] -= 1
                self.curMax = max(self.d.values())
                return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()