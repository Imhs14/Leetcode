class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        prev = 0
        for num in nums:
            ad = prev + num
            res.append(ad)
            prev = ad
        return res