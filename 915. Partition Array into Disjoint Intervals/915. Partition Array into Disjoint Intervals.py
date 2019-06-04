'''Approach 1: Next Array
Intuition

Instead of checking whether all(L <= R for L in left for R in right), let's check whether max(left) <= min(right).

Algorithm

Let's try to find max(left) for subarrays left = A[:1], left = A[:2], left = A[:3], ... etc. Specifically, maxleft[i] will be the maximum of subarray A[:i]. They are related to each other: max(A[:4]) = max(max(A[:3]), A[3]), so maxleft[4] = max(maxleft[3], A[3]).

Similarly, min(right) for every possible right can be found in linear time.

After we have a way to query max(left) and min(right) quickly, the solution is straightforward.'''

class Solution(object):
    def partitionDisjoint(self, A):
        N = len(A)
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in xrange(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in xrange(N-1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in xrange(1, N):
            if maxleft[i-1] <= minright[i]:
                return i

'''B[i] stands for the minimum value in subarray A[i], A[i+1], ..., A[n-1]
pmax stands for the prefix maximum of i first values in A.
return the smallest that i that pmax <= B[i]'''

def partitionDisjoint(self, A):
        B = A[:]
        n = len(A)
        for i in range(n - 1)[::-1]:
            B[i] = min(A[i], B[i + 1])
        pmax = 0
        for i in range(1,n):
            pmax = max(pmax, A[i-1])
            if pmax <= B[i]:
                return i