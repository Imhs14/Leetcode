# Question : 15. 3Sum
# Complexity : Time: O(N^2), Space: O(N)
# Topic/Category : Two Pointers
# Difficulty : Medium
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] > 0:
                break 
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            
            lo, hi = i + 1, n - 1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    ans.append([nums[i],nums[lo],nums[hi]])
                    lo,hi = lo+1,hi-1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif summ > 0:
                    hi -= 1
                else:
                    lo += 1
        return ans
# Time = O(n^2), Space = O(n)

"""
nums = [-1,0,1,2,-1,-4]
o/p = [[-1,-1,2],[-1,0,1]]
"""
