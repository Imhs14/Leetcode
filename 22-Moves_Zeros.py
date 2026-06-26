class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        L = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[L], nums[r] = nums[r], nums[L]
                L += 1
        # Time = O(n) , Space = O,(1), # Two pointers
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k,j = 0,0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                 nums[k]= nums[i]
                 k += 1
            else:
                j+=1
    
        while j > 0:
           nums[-j] = 0
           j-=1  
        # Time = O(n) , Space = O,(1), # Two pointers
"""
    