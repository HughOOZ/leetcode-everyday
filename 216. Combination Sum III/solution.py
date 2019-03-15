'''Batteries Included
AC in 44ms

First the obligatory "use the darn library" solution. Create all k-combinations of digits and keep those with sum n:'''
from itertools import combinations

class Solution:
    def combinationSum3(self, k, n):
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]
'''Recursive
AC in 48 ms

But it's more interesting to do it on your own. Here I use a recursive helper function getting the same k and n as the main function, and an additional cap under which all the numbers have to be:'''
class Solution:
    def combinationSum3(self, k, n):
        def combs(k, n, cap):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                    for last in range(1, cap)
                    for comb in combs(k-1, n-last, last)]
        return combs(k, n, 10)
'''Iterative
AC in 56 ms

And an iterative version doing pretty much the same thing, except this time I prepend elements on the left, and use the first element of a partial combination as the cap.'''
class Solution:
    def combinationSum3(self, k, n):
        combs = [[]]
        for _ in range(k):
            combs = [[first] + comb
                     for comb in combs
                     for first in range(1, comb[0] if comb else 10)]
        return [c for c in combs if sum(c) == n]
'''Reduce
AC in 44 ms

And here's a "one-liner" version of the iterative solution using reduce instead of the loop:'''
class Solution:
    def combinationSum3(self, k, n):
        return [c for c in
                reduce(lambda combs, _: [[first] + comb
                                         for comb in combs
                                         for first in range(1, comb[0] if comb else 10)],
                       range(k), [[]])
                if sum(c) == n]
'''Easy to understand Python solution (backtracking).
'''
def combinationSum3(self, k, n):
    res = []
    self.dfs(xrange(1,10), k, n, 0, [], res)
    return res
    
def dfs(self, nums, k, n, index, path, res):
    if k < 0 or n < 0: # backtracking 
        return 
    if k == 0 and n == 0: 
        res.append(path)
    for i in xrange(index, len(nums)):
        self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)

'''Concise python solution using DFS'''
class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if n > sum([i for i in range(1, 11)]):
            return []

        res = []
        self.sum_help(k, n, 1, [], res)
        return res


    def sum_help(self, k, n, curr, arr, res):
        if len(arr) == k:
            if sum(arr) == n:
                res.append(list(arr))
            return

        if len(arr) > k or curr > 9:
            return
        
        for i in range(curr, 10):
            arr.append(i)
            self.sum_help(k, n, i + 1, arr, res)
            arr.pop()
