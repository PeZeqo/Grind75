"""
Runtime 66% [set: O(1), get: O(log(n))]
Memory 84% O(N) (number of `set` operations)
"""


class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.data.get(key, [])
        values.append((timestamp, value))
        self.data[key] = values

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        values = self.data[key]

        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            midT = values[mid][0]
            midV = values[mid][1]

            if midT == timestamp:
                return midV
            elif midT > timestamp:
                r = mid - 1
            else:
                res = midV
                l = mid + 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
