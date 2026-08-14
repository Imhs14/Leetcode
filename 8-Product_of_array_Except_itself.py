# Question : 238. Product of Array Except Self
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Arrays & Hashing
# Difficulty : Medium
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        for i in range(n):
            j = -i -1 
            l_arr[i] = l_mult # the numbers before current number 1,2,3 we are at 1 and before 1 nth is there so default we take 1 l_mult = 1
            r_arr[j] = r_mult # the numbers after the current number 1,2,3, we are at 3 so after 3 nth is there so ans is 1 bcs  ## r_mult = 1
            l_mult *= nums[i]   # Prefix multipication except itself
            r_mult *= nums[j]   # suffix multipication except itself
        return [l*r for l,r in zip(l_arr, r_arr)]
# Time complexity = O(n)
# space complexity = O(n)
'''nums =
[1, 2, 3, 4]
Output
[24, 12, 8, 6]
'''
"""
nums = [1,2,3,4]
o/p = [24,12,8,6]
"""
