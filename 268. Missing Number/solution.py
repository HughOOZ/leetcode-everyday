class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

class MySolution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i