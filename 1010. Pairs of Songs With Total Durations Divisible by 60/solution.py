class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0
        for i in range(len(time)-1):
            for j in range(i+1,len(time)):
                if (time[i]+time[j])%60 == 0:
                    result += 1
        return result

'''Calculate the time % 60 then it will be exactly same as two sum problem.
t % 60 gets the remainder 0 ~ 59.
We count the occurrence of each remainders in a array/hashmap c.

we want to know that, for each t, how many x satisfy (t + x) % 60 = 0.

t % 60 + x % 60 = 60 for the most cases.

It has to be noticed that, if t % 60 = 0, x % 60 = 0 instead of 60.

60 - t % 60 will get a number in range 1 ~ 60.

(60 - t % 60) % 60 can get number in range 0 ~ 59'''

 def numPairsDivisibleBy60(self, time):
        c = collections.Counter()
        res = 0
        for t in time:
            res += c[-t % 60]
            c[t % 60] += 1
        return res