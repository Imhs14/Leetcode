# Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.
# Question : 2124. Check if All A's Appears Before All B's
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Mid Level,String, Weekly Contest 274
# Difficulty : Easy
class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i] == 'b' and s[i+1] == 'a':
                return False
        return True

p1 = Solution()

print(p1.checkString('aabb'))

print(p1.checkString('baabb'))

print(p1.checkString('bbbb'))