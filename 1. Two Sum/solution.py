class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums:
                if 2*nums[i] != target:
                    return [i,nums.index(target-nums[i])]
                elif nums[i] in nums[i+1:]:
                    return [i,nums[i+1:].index(nums[i])+i+1]