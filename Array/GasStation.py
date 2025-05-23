"""
Solution:
Runtime 71% O(N)
Memory 13% O(1)

Attempt 1:
Runtime 43% O(N)
Memory 44% O(1)

Attempt 1:
Runtime 5% O(N^2)
Memory 5% O(N)
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        subSum = 0
        if sum(cost) > sum(gas):
            return -1

        for ind in range(len(gas)):
            subSum += (gas[ind] - cost[ind])
            if subSum < 0:
                start = ind + 1
                subSum = 0

        return start

    def canCompleteCircuitAttempt2(self, gas: List[int], cost: List[int]) -> int:
        start = None
        subSum = 0
        net = 0
        for ind in range(len(gas)):
            if start is None:
                start = ind

            value = gas[ind] - cost[ind]
            net += value
            subSum += value
            if subSum < 0:
                start = None
                subSum = 0

        if start is None or net < 0:
            return -1
        return start

    def canCompleteCircuitAttempt1(self, gas: List[int], cost: List[int]) -> int:
        moveThrough = [gas[i] - cost[i] for i in range(len(gas))]
        bestStart = [-1] * len(gas)
        start = None
        subSum = 0
        for ind, value in enumerate(moveThrough):
            if start is None:
                start = ind
            subSum += value
            if subSum < 0:
                start = None
                subSum = 0
                continue
            else:
                bestStart[ind] = start

        if bestStart[-1] == -1:
            return -1

        ind = bestStart[-1]
        curGas = 0
        start = ind
        leftStart = False
        while curGas >= 0 or not leftStart:
            if leftStart and ind == start:
                return start

            curGas += gas[ind]
            curGas -= cost[ind]
            ind += 1
            if ind >= len(gas):
                ind = 0

            leftStart = True

        return -1
