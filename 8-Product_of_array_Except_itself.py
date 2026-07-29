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
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
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
