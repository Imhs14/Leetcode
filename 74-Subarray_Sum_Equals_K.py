# Question : 560. Subarray Sum Equals K
# Complexity : Time: O(N), Space: O(n)
# Topic/Category : Senior Staff,Array,Hash Table,Prefix Sum
# Difficulty : Medium
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        m = {}
        for j in range(n):
            v = prefix_sum[j] - k

            if prefix_sum[j] == k:
                count += 1
            
            if v in m:
                count += m[v]
            
            if prefix_sum[j] not in m:
                m[prefix_sum[j]] = 0
            m[prefix_sum[j]] += 1
        return count

p = Solution()

print(p.subarraySum([1,1,1],2))

print(p.subarraySum([1,2,3],3))