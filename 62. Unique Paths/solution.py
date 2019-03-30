class MySolution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(self.factorial(m+n-2)/self.factorial(m-1)/self.factorial(n-1))
    
    def factorial(self,num):
        result = 1
        for i in range(1,num+1):
            result *= i
        return result

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]