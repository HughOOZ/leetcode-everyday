class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i+1]==nums[i]:
                return nums[i]

'''Approach #3 Floyd's Tortoise and Hare (Cycle Detection) [Accepted]
Intuition

If we interpret nums such that for each pair of index ii and value v_iv 
i
​   
 , the "next" value v_jv 
j
​   
  is at index v_iv 
i
​   
 , we can reduce this problem to cycle detection. See the solution to Linked List Cycle II for more details.

Algorithm

First off, we can easily show that the constraints of the problem imply that a cycle must exist. Because each number in nums is between 11 and nn, it will necessarily point to an index that exists. Therefore, the list can be traversed infinitely, which implies that there is a cycle. Additionally, because 00 cannot appear as a value in nums, nums[0] cannot be part of the cycle. Therefore, traversing the array in this manner from nums[0] is equivalent to traversing a cyclic linked list. Given this, the problem can be solved just like Linked List Cycle II.

To see the algorithm in action, check out the animation below:

'''
class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1