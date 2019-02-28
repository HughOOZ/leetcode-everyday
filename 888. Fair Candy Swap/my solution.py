class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a = sum(A) - sum(B)
        a = int(a/2)
        for i in range(len(A)):
            if (A[i]-a) in B:
                return [A[i],A[i]-a]
