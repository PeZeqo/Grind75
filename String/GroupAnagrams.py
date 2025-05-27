"""
Solution:
Runtime 83% O(N * Klog(K)) (K is average length of string)
Memory 53% O(N)

Attempt 2:
Runtime 8% O(N^2)
Memory 5% O(N)

Attempt 1:
Runtime 7% O(N^2)
Memory 5% O(N)
"""

import random


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)

        for str in strs:
            out[''.join(sorted(str))].append(str)

        return list(out.values())

    def groupAnagramsAttempt2(self, strs: List[str]) -> List[List[str]]:
        dicts = defaultdict(list)
        for ind, str in enumerate(strs):
            d = defaultdict(int)
            count = 0
            for c in str:
                d[c] += 1
                count += ord(c)
            dicts[count].append((ind, d))

        out = []
        for lst in dicts.values():
            while lst:
                compare = lst[0]
                row = [strs[compare[0]]]
                toReCheck = []
                for ind, other in enumerate(lst[1:]):
                    if compare[1] == other[1]:
                        row.append(strs[other[0]])
                    else:
                        toReCheck.append(other)
                out.append(row)
                lst = toReCheck

        return out

    def groupAnagramsAttempt1(self, strs: List[str]) -> List[List[str]]:
        dicts = defaultdict(list)
        for ind, str in enumerate(strs):
            d = defaultdict(int)
            count = 0
            for c in str:
                d[c] += 1
                count += ord(c)
            dicts[count].append((ind, d))

        out = []
        for lst in dicts.values():
            while lst:
                if len(lst) == 1:
                    out.append([strs[lst[0][0]]])
                    break
                compare = lst[0]
                row = [strs[compare[0]]]
                toRemove = [0]
                for ind, other in enumerate(lst[1:]):
                    if compare[1] == other[1]:
                        row.append(strs[other[0]])
                        toRemove.append(ind + 1)
                out.append(row)
                if len(toRemove) == len(lst):
                    break
                else:
                    for remove in toRemove[::-1]:
                        lst.pop(remove)

        return out
