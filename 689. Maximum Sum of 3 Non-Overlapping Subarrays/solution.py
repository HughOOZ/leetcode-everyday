'''A greedy solution using three sliding windows where you keep track of the best indexes/sums as you go.

O(n) time: Since we're only going through the list once and using no complex operations, this is O(n).
O(1) space: Just a fixed set of temp vars. We don't need the extra arrays that the DP solutions have.'''

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k*2]

        # Sums of each window
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k*2])
        seqThreeSum = sum(nums[k*2:k*3])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k*2 + 1
        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]
            
            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1

        return bestThreeSeq

'''Approach #1: Ad-Hoc [Accepted]
Intuition

It is natural to consider an array W of each interval's sum, where each interval is the given length K. To create W, we can either use prefix sums, or manage the sum of the interval as a window slides along the array.

From there, we approach the reduced problem: Given some array W and an integer K, what is the lexicographically smallest tuple of indices (i, j, k) with i + K <= j and j + K <= k that maximizes W[i] + W[j] + W[k]?

Algorithm

Suppose we fixed j. We would like to know on the intervals i \in [0, j-K]i∈[0,j−K] and k \in [j+K, \text{len}(W)-1]k∈[j+K,len(W)−1], where the largest value of W[i]W[i] (and respectively W[k]W[k]) occurs first. (Here, first means the smaller index.)

We can solve these problems with dynamic programming. For example, if we know that ii is where the largest value of W[i]W[i] occurs first on [0, 5][0,5], then on [0, 6][0,6] the first occurrence of the largest W[i]W[i] must be either ii or 66. If say, 66 is better, then we set best = 6.

At the end, left[z] will be the first occurrence of the largest value of W[i] on the interval i \in [0, z]i∈[0,z], and right[z] will be the same but on the interval i \in [z, \text{len}(W) - 1]i∈[z,len(W)−1]. This means that for some choice j, the candidate answer must be (left[j-K], j, right[j+K]). We take the candidate that produces the maximum W[i] + W[j] + W[k].'''

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in xrange(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans
