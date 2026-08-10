class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hsh = {}
        j = 1
        for i in range(len(nums)):
            hsh[nums[i]] = j
            j += 1
    
        for i in range(1,len(nums)+1):
            if i not in hsh:
                return i
            elif i == len(nums):
                return len(nums) +1

# Time = O(n), Space = O(n)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Loop 1: clean the array — replace anything out of range [1, n] with n+1
        for i in range(n):
            if nums[i] > n and nums[i] <= 0:
                nums[i] = n + 1

        # Loop 2: mark the presence — negate nums[num-1] if num is in range
        for i in range(n):
            num = abs(nums[i])
            if num > n:
                continue
            if nums[num - 1] > 0:
                nums[num - 1] *= -1

        # Loop 3: find the first missing positive — first index still positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

# Time = O(n), Space = O(1)