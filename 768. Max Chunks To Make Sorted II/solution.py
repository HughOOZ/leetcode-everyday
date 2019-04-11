'''Approach #1: Sliding Window [Accepted]
Intuition

Let's try to find the smallest left-most chunk.

Algorithm

Notice that if a_1, a_2, \dots, a_ma 
1
​	
 ,a 
2
​	
 ,…,a 
m
​	
  is a chunk, and a_1, a_2, \dots, a_na 
1
​	
 ,a 
2
​	
 ,…,a 
n
​	
  is a chunk (m < nm<n), then a_{m+1}, a_{m+2}, \dots, a_na 
m+1
​	
 ,a 
m+2
​	
 ,…,a 
n
​	
  is a chunk too. This shows that a greedy approach produces the highest number of chunks.

We know the array arr should end up like expect = sorted(arr). If the count of the first k elements minus the count what those elements should be is zero everywhere, then the first k elements form a valid chunk. We repeatedly perform this process.

We can use a variable nonzero to count the number of letters where the current count is non-zero.

'''
class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.defaultdict(int)
        ans = nonzero = 0

        for x, y in zip(arr, sorted(arr))
            count[x] += 1
            if count[x] == 0: nonzero -= 1
            if count[x] == 1: nonzero += 1

            count[y] -= 1
            if count[y] == -1: nonzero += 1
            if count[y] == 0: nonzero -= 1

            if nonzero == 0: ans += 1

        return ans

'''Approach #2: Sorted Count Pairs [Accepted]
Intuition

As in Approach #1, let's try to find the smallest left-most chunk, where we have some expectation expect = sorted(arr)

If the elements were distinct, then it is enough to find the smallest k with max(arr[:k+1]) == expect[k], as this must mean the elements of arr[:k+1] are some permutation of expect[:k+1].

Since the elements are not distinct, this fails; but we can amend the cumulative multiplicity of each element to itself to make the elements distinct.

Algorithm

Instead of elements x, have counted elements (x, count) where count ranges from 1 to the total number of x present in arr.

Now cur will be the cumulative maximum of counted[:k+1], where we expect a result of Y = expect[k]. We count the number of times they are equal.

'''
class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, None
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X)
            if cur == Y:
                ans += 1
        return ans

def maxChunksToSorted(self, arr):
        res, c1, c2 = 0, collections.Counter(), collections.Counter()
        for a, b in zip(arr, sorted(arr)):
            c1[a] += 1
            c2[b] += 1
            res += c1 == c2
        return res
