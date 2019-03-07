def arrayNesting(self, nums):
        seen, res = [0] * len(nums), 0
        for i in nums:
            count, j = 0, i
            while not seen[j]:
                seen[j], count, j = 1, count + 1, nums[j]
            res = max(res, count)
        return res

