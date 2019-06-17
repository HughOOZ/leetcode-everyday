class MySolution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        result = 0
        for i in range(len(A)-1):
            if A[i] >= A[i+1]:
                result += A[i] - A[i+1] + 1
                A[i+1] = A[i] +1
        return result

'''Solution 1: Just Sort, O(NlogN)
Sort the input array.
Compared with previous number,
the current number need to be at least prev + 1.

Time Complexity: O(NlogN) for sorting
Space: O(1) for in-space sort

Note that you can apply "O(N)" sort in sacrifice of space.
Here we don't talk further about sort complexity.
'''
def minIncrementForUnique(self, A):
        res = need = 0
        for i in sorted(A):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res


'''Solution 2, O(KlogK)
Same idea as solution 1 above.
But instead of assign value one by one,
we count the input numbers first, and assign values to all same value at one time.

This solution has only O(N) time for cases like [1,1,1,1,1,1,.....]

Time Complexity:
O(NlogK) using TreeMap in C++/Java
O(N + KlogK) using HashMap in Python
Space: O(K) for in-space sort'''

def minIncrementForUnique(self, A):
        c = collections.Counter(A)
        res = need = 0
        for x in sorted(c):
            res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) / 2
            need = max(need, x) + c[x]
        return res

'''Solution 3: Union Find, O(N)
Time: average O(N)
Space: O(N)'''

def minIncrementForUnique(self, A):
        root = {}
        def find(x):
            if x not in root:
                root[x] = x
            elif x != root[x]:
                root[x] = find(root[x])
            elif x + 1 in root:
                root[x] = find(root[x + 1])
            else:
                root[x] = root[x + 1] = x + 1
            return root[x]
        return sum(find(a) - a for a in A)