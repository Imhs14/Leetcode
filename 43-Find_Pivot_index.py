class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i in range(0, len(nums)):
            a = total - leftsum - nums[i]
            if a == leftsum:
                return i
            leftsum += nums[i]
        return -1
# Time = O(N), Space = O(1)