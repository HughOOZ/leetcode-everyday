class MySolution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        def solution(nums,num):
            for i in range(len(nums)-1,-1,-1):
                if nums[i]==num:
                    return i-nums.index(num)+1
        
        result = []
        counts = collections.Counter(nums)
        frequency = max(counts.values())
        for i,j in counts.items():
            if j==frequency:
                result.append(solution(nums,i))
        if len(result) > 1:
            return min(result)
        else:
            return result[0]

'''Approach #1: Left and Right Index [Accepted]
Intuition and Algorithm

An array that has degree d, must have some element x occur d times. If some subarray has the same degree, then some element x (that occured d times), still occurs d times. The shortest such subarray would be from the first occurrence of x until the last occurrence.

For each element in the given array, let's know left, the index of its first occurrence; and right, the index of its last occurrence. For example, with nums = [1,2,3,2,5] we have left[2] = 1 and right[2] = 3.

Then, for each element x that occurs the maximum number of times, right[x] - left[x] + 1 will be our candidate answer, and we'll take the minimum of those candidates.'''
class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
