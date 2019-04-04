'''Solution 1:
Try all possibilities from 1 to 6'''

def minDominoRotations(self, A, B):
        for x in range(1, 7):
            if all(x == a or x == b for a, b in zip(A, B)):
                return min(len(A) - A.count(x), len(B) - B.count(x))
        return -1

'''Solution 2
Try A[0]
Try B[0]
return -1
One observation is that, if A[0] works, no need to check B[0].
Because if both A[0] and B[0] exist in all dominoes,
the result will be the same'''

'''Solution 3
Find intersection set s of {A[i], B[i]}
s.size = 0, no possible result.
s.size = 1, one and only one result.
s.size = 2, it means all dominoes are [a,b] or [b,a], try either one.
s.size > 2, impossible'''
def minDominoRotations(self, A, B):
        s = reduce(set.__and__, [set(d) for d in zip(A, B)])
        if not s: return -1
        x = s.pop()
        return min(len(A) - A.count(x), len(B) - B.count(x))