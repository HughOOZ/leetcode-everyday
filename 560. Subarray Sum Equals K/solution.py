'''Let's remember count[V], the number of previous prefix sums with value V. If our newest prefix sum has value W, and W-V == K, then we add count[V] to our answer.

This is because at time t, A[0] + A[1] + ... + A[t-1] = W, and there are count[V] indices j with j < t-1 and A[0] + A[1] + ... + A[j] = V. Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.'''
def subarraySum(self, A, K):
    count = collections.Counter()
    count[0] = 1
    ans = su = 0
    for x in A:
        su += x
        ans += count[su-K]
        count[su] += 1
    return ans

def subarraySum(self, nums, k):
        count, cur, res = {0: 1}, 0, 0
        for v in nums:
            cur += v
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res

'''Great solution. Explained the same/similar solution with explanation why this works. Hope this helps.
https://www.youtube.com/watch?v=vrmcXLYRt9Y'''

