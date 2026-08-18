# Question : GFG. Strong Number
# Complexity : Time: O(D), Space: O(1)
# Topic/Category : Math
# Difficulty : Easy
import math
class Solution:
    def isStrong(self, n):
        # code here
        s = str(n)
        v = 0
        for i in range(0,len(s)):
            z = math.factorial(int(s[i]))
            v += z

        return v==n

"""
input = 145
Output: true

Explanation: The sum of the factorials of its digits is: 1! + 4! + 5! = 1 + 24 + 120 = 145.
Since the sum equals the original number, 145 is a Strong Number
"""