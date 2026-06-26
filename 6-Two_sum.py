# LeetCode Problem 1: Two Sum
# URL: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Category: Arrays & Hashing
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {nums[0]: 0}
        for i in range(1,len(nums)):
            a = target - nums[i]
            if a in seen.keys() and (i != seen[a]):
                return [i,seen[a]]
            
            seen[nums[i]] = i 