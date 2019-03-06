class MySolution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        for i in range(len(timeSeries)):
            if i == len(timeSeries)-1:
                result += duration
                break
            elif timeSeries[i]+duration <= timeSeries[i+1]:
                result += duration
            else:
                result += timeSeries[i+1]-timeSeries[i]
        return result

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        if len(timeSeries) == 1:
            return duration
        ans = duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i] > timeSeries[i-1] + duration - 1:
                ans += duration
            else:
                ans += timeSeries[i] - timeSeries[i-1] 
        return ans
