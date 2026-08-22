# Question : 136. Single Number
# Complexity : Time: O(N), Space: O(n)
# Topic/Category : Array, Bit Manipulation
# Difficulty : Easy
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hsh = {}
        for i in range(len(nums)):
            if nums[i] not in hsh.keys():
                hsh[nums[i]] = 1
            else:
                hsh[nums[i]] += 1

        result = min(hsh,key = lambda x: hsh[x])
        return result

p1 = Solution()

print(p1.singleNumber([4,1,2,1,2]))

print(p1.singleNumber([2,2,1]))