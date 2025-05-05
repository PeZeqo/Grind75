"""
Solution:
Runtime 93% O(n^2)
Memory 6% O(n)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p, z, n = [], [], []
        res = set()

        for num in nums:
            if num < 0:
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                z.append(num)

        if len(z) > 2:
            res.add((0, 0, 0))

        N = set(n)
        P = set(p)

        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
            for num in N:
                if -num in P:
                    res.add((num, 0, -num))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                total = abs(n[i] + n[j])
                if total in P:
                    res.add(tuple(sorted([n[i], n[j], total])))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                total = -1 * (p[i] + p[j])
                if total in N:
                    res.add(tuple(sorted([p[i], p[j], total])))

        return [list(l) for l in res]
