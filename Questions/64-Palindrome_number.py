# Question : 9. Palindrome Number
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Math
# Difficulty : Easy
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        elif x == 0:
            return True
        m = x
        res = 0
        while m > 0:
            digit = m % 10
            res = res * 10 + digit
            m //= 10
        return res == x 