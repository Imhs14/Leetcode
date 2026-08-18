# Question : 344. Reverse String
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Two Pointers
# Difficulty : Easy
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        for i in range(len(s) // 2):
                s[i], s[j] = s[j], s[i]
                j -= 1    
# Time = O(N), Space = O(1)
"""
s = ["h","e","l","l","o"]
o/p = ["o","l","l","e","h"]
"""
