class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

 class MySolution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        for each in nums:
            if nums.count(each) > length/2:
                return each