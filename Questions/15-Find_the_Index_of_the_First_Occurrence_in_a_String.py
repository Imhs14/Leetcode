# Question : 28. Find the Index of the First Occurrence in a String
# Complexity : Time: O(N * M), Space: O(1)
# Topic/Category : Strings
# Difficulty : Easy
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1
        for i in range(0, len(haystack)) :
            if haystack[i:i + len(needle) ] == needle:
                return i
'''haystack =
"sadbutsad"
needle =
"sad"
Output
0
'''
"""
haystack = "sadbutsad"
needle = "sad"
o/p = 0
"""
