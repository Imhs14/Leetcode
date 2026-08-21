# Question : 26. Remove Duplicates from Sorted Array
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Two Pointers
# Difficulty : Easy
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
            else:
                i += 1
            
        return len(nums) 
    # time O(n^2)
    #space O(1)
    # Better and Optimal solution 
    '''    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k    ''' 
    # time O(n)
    # space O(1)
'''nums =
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output
5
'''
"""
nums = [1,1,2]
o/p = 2
"""
