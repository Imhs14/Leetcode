# Question : 389. Find the Difference
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Junior, Hash Table, String, Bit Manipulation,Sorting
# Difficulty : Easy
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_ad = 0
        t_ad = 0
        for i in range(len(t)):
            t_ad += ord(t[i])
        for j in range(len(s)):
            s_ad += ord(s[j])

        return chr(t_ad - s_ad)
p = Solution()

print(p.findTheDifference('a','aa'))