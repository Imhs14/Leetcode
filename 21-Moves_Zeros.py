class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        L = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[L], nums[r] = nums[r], nums[L]
                L += 1
            