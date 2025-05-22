"""
Solution (math):
Runtime 95% O(N) (sort runs on constant space data so O(26log26) ~= O(1))
Memory 57% O(1)

Attempt1 (max heap):
Runtime 23% O(N)
Memory 88% O(N)
"""

import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        freq.sort()
        chunk = freq[-1] - 1
        idle = chunk * n
        for num in freq[-2::-1]:
            idle -= min(chunk, num)

        return len(tasks) + idle if idle >= 0 else len(tasks)

    def leastIntervalAttempt1(self, tasks: List[str], n: int) -> int:
        taskCounts = defaultdict(int)
        for task in tasks:
            taskCounts[task] -= 1

        heap = []
        for key, count in taskCounts.items():
            heapq.heappush(heap, (count, key))

        cooldown = {}
        time = 0
        while cooldown or heap:
            time += 1
            if time in cooldown:
                heapq.heappush(heap, cooldown[time])
                del cooldown[time]

            if heap:
                count, task = heapq.heappop(heap)
                if count < -1:
                    cooldown[time + n + 1] = (count + 1, task)

        return time
