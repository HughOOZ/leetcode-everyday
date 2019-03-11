class MySolution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            if sorted(arr[:i]) == [i for i in range(i)]:
                result +=1
        return result

class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans
