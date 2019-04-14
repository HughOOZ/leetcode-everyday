class MySolution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        num = ''
        for each in A:
            num += str(each)
            if int(num,2)%5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result

'Calculate Prefix Mod'
def prefixesDivBy5(self, A):
        for i in xrange(1, len(A)):
            A[i] += A[i - 1] * 2 % 5
        return [a % 5 == 0 for a in A]