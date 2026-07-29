from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        hsh = defaultdict(int)
        for i in range(0,len(nums)):
            hsh[nums[i]] += 1 

        for key, value in hsh.items():
            if value % 2:
                ans.append(key)
        return ans

# time = O(n), space = O(n)

"""
nums = [1,2,1,3,2,5]

o/p = [3,5]

"""