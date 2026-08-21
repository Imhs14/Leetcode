# Question : 680. Valid Palindrome II
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Two Pointers
# Difficulty : Easy
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checker(s,lo,hi):
            while lo < hi:
                if s[lo] == s[hi]:
                    lo += 1
                    hi -= 1
                else:
                    return False
            return True

        i,j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            elif checker(s,i+1,j) or checker(s,i,j-1):
                return True
            else:
                return False
        return True
"""
Input: s = "aba"
Output: true

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Input: s = "abc"
Output: false

Input: s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
Output: true

Input: s = "zryxeededexyz"
Output: false

"""