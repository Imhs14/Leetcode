# Question : 27. Remove Element
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Two Pointers
# Difficulty : Easy

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

""" My solution at first 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = len(nums)
        i = 0
        while i < s:
            if nums[i] == val:
                nums.remove(nums[i])
                s -= 1
            elif nums[i]] != val:
                i += 1
        
"""

'''
nums =
[3, 2, 2, 3]

val =
3

Output
2
'''