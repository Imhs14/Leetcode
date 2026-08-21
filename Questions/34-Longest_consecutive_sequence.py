# Question : 128. Longest Consecutive Sequence
# Complexity : Time: O(N), Space: O(N)
# Topic/Category : Arrays & Hashing
# Difficulty : Medium
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0 
        for num in s:
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest
# Time = O(n), Space = O(n)
"""
nums = [100,4,200,1,3,2]
o/p = 4
"""
