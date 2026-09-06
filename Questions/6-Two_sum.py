# Question : 1. Two Sum
# Complexity : Time: O(N), Space: O(N)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {nums[0]: 0}
        for i in range(1,len(nums)):
            a = target - nums[i]
            if a in seen.keys():
                return [i,seen[a]]
            
            seen[nums[i]] = i
p = Solution()
print(p.twoSum([1, 3, 5, -7, 6, -3],0))
'''nums =
[2, 7, 11, 15]
target =
9
Output
[0, 1]
'''
"""
nums = [2,7,11,15]
target = 9
o/p = [0,1]
"""
