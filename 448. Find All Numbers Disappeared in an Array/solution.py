class Solution:
    def findDisappearedNumbers(self, nums):
        ret = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i + 1)
        return ret

class MySolution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        for each in nums:
            result[each-1] += 1
        result = [i+1 for i in range(len(nums)) if result[i] ==0]
        return result
