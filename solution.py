def arrayNesting(self, nums):
        seen, res = [0] * len(nums), 0
        for i in nums:
            count, j = 0, i
            while not seen[j]:
                seen[j], count, j = 1, count + 1, nums[j]
            res = max(res, count)
        return res

class MySolution:
    """
    Time Limit Exceeded
    """
    def arrayNesting(self, nums: List[int]) -> int:
        results = []
        for i in range(len(nums)):
            result = set()
            while i not in result:
                result.add(i)
                i = nums[i]
            results.append(len(result))
        return max(results)
