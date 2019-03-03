class MySolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        zero = 0
        result = 1
        pos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                pos = i
                continue
            result *= nums[i]
        if zero == 1:
            results = [0]*len(nums)
            results[pos] = result
            return results
        if zero >= 2:
            return [0]*len(nums)
        if zero == 0:
            for each in nums:
                results.append(int(result/each))
            return results


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output