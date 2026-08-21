# Question : 414. Third Maximum Number
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Arrays
# Difficulty : Easy
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3: return max(nums)
        fmx = float("-inf")
        smx = float("-inf")
        tmx = float("-inf")
        for num in nums:
            if num > fmx:
                fmx,smx,tmx = num,fmx,smx
            elif num > smx and num != fmx:
                smx,tmx = num,smx
            elif num > tmx and num != smx and num != fmx:
                tmx = num
        return min(fmx,smx,tmx)
# Time = O(n), Space = O(1)
"""
nums = [3,2,1]
o/p = 1
"""