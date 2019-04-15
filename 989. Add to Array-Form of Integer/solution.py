'''Explanation
Take K as a carry.
Add it to the lowest digit,
Update carry K,
and Keep going to higher digit.

Time Complexity

Insert will take O(1) time or O(N) time on shifting, depending on the data stucture.
But in this problem K is at most 5 digit so this is restricted.
So this part doesn't matter.

The overall time complexity is O(N)'''

def addToArrayForm(self, A, K):
        for i in range(len(A))[::-1]:
            A[i], K = (A[i] + K) % 10, (A[i] + K) / 10
        return [int(i) for i in str(K)] + A if K else A