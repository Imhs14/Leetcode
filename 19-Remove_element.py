class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k           

# Time  = O(n), Space = O(1), Solved using Two pointer 

"""
nums =
[0,1,2,2,3,0,4,2]
val =
2
Output = [0,1,4,0,3] 
"""