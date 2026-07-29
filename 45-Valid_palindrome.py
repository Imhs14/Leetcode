class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        i = 0
        while i < j :
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if (s[i].lower()) != (s[j].lower()):
                return False
            i += 1
            j -= 1
        return True
# Time = O(n), Space = O(1)
"""
s = "A man, a plan, a canal: Panama"
o/p = True
"""
