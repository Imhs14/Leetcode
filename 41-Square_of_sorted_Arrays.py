class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l] ** 2)
                l += 1
            else:
                res.append(nums[r] ** 2)
                r -= 1
        
        res.reverse()
        return res
# Time = O(n), Space = O(n) 
"""
nums = [-4,-1,0,3,10]
o/p = [0,1,9,16,100]
"""
