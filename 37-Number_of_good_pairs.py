# Question : 1512. Number of Good Pairs
# Complexity : Time: O(N), Space: O(N)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i] == nums[j] and i < j:
                    output += 1
        return output
# Time : O(n), Space : O(n) Optimized solution

# These both are brute force Time :O(n^2), Space : O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)): # here as we don't need to see 1st element again so we are starting at 1 and not at 0
                if i != j  :
                    if nums[i] == nums[j] and i < j:
                        a = (nums[i], nums[j])
                        output.append(a)
        return len(output)
 # Optimized solution is still not done
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i] == nums[j] and i < j:
                    output += 1
        return output
"""
nums = [1,2,3,1,1,3]
o/p = 4
"""
