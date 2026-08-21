# Question : 53. Maximum Subarray
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Dynamic Programming / Kadane's Algorithm
# Difficulty : Medium
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = cur_sum = nums[0]
        
        for i in range(1,len(nums)):
            cur_sum = max(nums[i],cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)

        return max_sum

# Time = O(n), Space = O(1)