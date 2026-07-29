class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(0, n):
            res.extend([nums[i], nums[n+i]])
        return res
# Time = O(n), Space = O(n)
# case 1 
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        i = 0 
        while i < n:
            res.append(nums[i])
            res.append(nums[n+i])
            i += 1
        return res
    
# case 2
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(0, n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
"""
nums = [2,5,1,3,4,7]
n = 3
o/p = [2,3,5,4,1,7]
"""
