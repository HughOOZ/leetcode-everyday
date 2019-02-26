class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        while len(A)>= 3:
            if A[-1] < A[-2] + A[-3]:
                return A[-1]+A[-2]+A[-3]
            else:
                A.pop()
        return 0
