class MySolution:
    def isMonotonic(self, A: List[int]) -> bool:
        B = A[:]
        C = A[:]
        B.sort()
        C.sort(reverse=True)
        if A==B or A==C:
            return True
        return False

class Solution(object):
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in xrange(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in xrange(len(A) - 1)))
