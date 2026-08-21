# Question : 448. Find All Numbers Disappeared in an Array
# Complexity : Time: O(N), Space: O(N)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1))-set(nums))
"""
My other trys
case : 1
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        z = set(range(1, len(nums)+1))
        y = set(nums)
        
        return list(z-y)
        
case : 2
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        # Loop 2: find indices that are still positive
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result"""
'''nums =
[4, 3, 2, 7, 8, 2, 3, 1]
Output
[5, 6]
'''
"""
nums = [4,3,2,7,8,2,3,1]
o/p = [5,6]
"""
