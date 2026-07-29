class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        prev = 0
        for num in nums:
            ad = prev + num
            res.append(ad)
            prev = ad
        return res
# Time = O(n), Space  = O(n)
"""
nums = [1,2,3,4]
o/p = [1,3,6,10]
"""
