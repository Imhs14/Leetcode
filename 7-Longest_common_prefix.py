# LeetCode Problem 14: Longest Common Prefix
# URL: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Category: Strings
# Time Complexity: O(N * M)
# Space Complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        seen = ''
        for positions in range(len(min(strs))):
            for string in strs:
                if string[positions] != strs[0][positions]:
                    return ''
            
            seen += (strs[0][positions])
        return seen