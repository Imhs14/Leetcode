# LeetCode Problem 28: Find the Index of the First Occurrence in a String
# URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Difficulty: Easy
# Category: Strings
# Time Complexity: O(N * M)
# Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1
        for i in range(0, len(haystack)) :
            if haystack[i:i + len(needle) ] == needle:
                return i