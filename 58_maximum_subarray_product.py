# Question : 152. Maximum Product Subarray
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Dynamic Programming
# Difficulty : Medium
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        max_prod = nums[0]
        prev_max = prev_min = nums[0]

        for i in range(1,n):
            prev_max, prev_min = max(nums[i], prev_min * nums[i], prev_max * nums[i]), min(nums[i], prev_min * nums[i], prev_max * nums[i])

            max_prod = max(max_prod, prev_min, prev_max)
            
        return max_prod

# Time = O(n), Space = O(1)