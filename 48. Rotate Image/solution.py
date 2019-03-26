'''Most Pythonic - [::-1] and zip - 44 ms

The most pythonic solution is a simple one-liner using [::-1] to flip the matrix upside down and then zip to transpose it. It assigns the result back into A, so it's "in-place" in a sense and the OJ accepts it as such, though some people might not.'''
class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
