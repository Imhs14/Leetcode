"""class Solution:
    def twosum(self,nums,target):
        seen = {nums[0]:0}
        for i in range(1,len(nums)):
            a = target - nums[i]
            if a in seen.keys():
                return [seen[a],i]

            seen[nums[i]] = i

s = Solution()
print(s.twosum([2, 7, 11, 15],9))
print(s.twosum([1, 3, 5, -7, 6, -3],0))"""

# Longest common prefix
"""
class solve:
    def longestprefix(self,strs):
        seen = ''
        for positions in range(len(min(strs))):
            for string in strs:
                if string[positions] != strs[0][positions]:
                    return seen

            seen += strs[0][positions]
        return seen

p = solve()
print(p.longestprefix(["flower", "flow", "flight"]))"""
