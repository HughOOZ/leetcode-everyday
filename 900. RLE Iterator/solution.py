class RLEIterator(object):

    def __init__(self, A):
        self.A = A
        self.i = 0
        self.q = 0

    def next(self, n):
        while self.i < len(self.A):
            if self.q + n > self.A[self.i]:
                n -= self.A[self.i] - self.q
                self.q = 0
                self.i += 2
            else:
                self.q += n
                return self.A[self.i+1]
        return -1

class MyRLEIterator:

    def __init__(self, A: List[int]):
        self.B = []
        for i in range(0,len(A),2):
            self.B += A[i]*[A[i+1]]
        self.num = 0
        
    def next(self, n: int) -> int:
        self.num += n
        if self.num < len(self.B):
            return self.B[self.num-1]
        else:
            return -1
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
