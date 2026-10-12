# Question : 14. Longest Common Prefix
# Complexity : Time: O(N * M), Space: O(1)
# Topic/Category : Strings
# Difficulty : Easy
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        seen = ''
        for positions in range(len(min(strs))):
            for string in strs:
                print(string[positions],' ',strs[0][positions])
                if string[positions] != strs[0][positions]:
                    return seen
            
            seen += (strs[0][positions])
        return seen
'''strs =
["flower", "flow", "flight"]
Output
"fl"
'''
"""
strs = ["flower","flow","flight"]
o/p = "fl"
"""
p = Solution()
print(p.longestCommonPrefix(["flower", "flow", "flight"]))