'''Approach 1: Prefix Sums and Counting
Intuition

As is typical with problems involving subarrays, we use prefix sums to add each subarray. Let P[i+1] = A[0] + A[1] + ... + A[i]. Then, each subarray can be written as P[j] - P[i] (for j > i). Thus, we have P[j] - P[i] equal to 0 modulo K, or equivalently P[i] and P[j] are the same value modulo K.

Algorithm

Count all the P[i]'s modulo K. Let's say there are C_xC 
x
​   
  values P[i] \equiv x \pmod{K}P[i]≡x(modK). Then, there are \sum_x \binom{C_x}{2}∑ 
x
​   
 ( 
2
C 
x
​   
 
​   
 ) possible subarrays.

For example, take A = [4,5,0,-2,-3,1] and K = 5. Then P = [0,4,9,9,7,4,5], and C_0 = 2, C_2 = 1, C_4 = 4C 
0
​   
 =2,C 
2
​   
 =1,C 
4
​   
 =4:

With C_0 = 2C 
0
​   
 =2 (at P[0]P[0], P[6]P[6]), it indicates \binom{2}{2} = 1( 
2
2
​   
 )=1 subarray with sum divisible by KK, namely A[0:6] = [4, 5, 0, -2, -3, 1]A[0:6]=[4,5,0,−2,−3,1].
With C_4 = 4C 
4
​   
 =4 (at P[1]P[1], P[2]P[2], P[3]P[3], P[5]P[5]), it indicates \binom{4}{2} = 6( 
2
4
​   
 )=6 subarrays with sum divisible by KK, namely A[1:2]A[1:2], A[1:3]A[1:3], A[1:5]A[1:5], A[2:3]A[2:3], A[2:5]A[2:5], A[3:5]A[3:5].'''

 class Solution(object):
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return sum(v*(v-1)/2 for v in count.values())

'''Calculate the prefix sum and count it.'''

   def subarraysDivByK(self, A, K):
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res