# LeetCode Problem 26: Remove Duplicates from Sorted Array
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Category: Two Pointers
# Time Complexity: O(N)
# Space Complexity: O(1)

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
    '''
    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k    ''' 
    # time O(n)
    # space O(1)