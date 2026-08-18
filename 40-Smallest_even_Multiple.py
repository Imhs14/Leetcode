# Question : 2413. Smallest Even Multiple
# Complexity : Time: O(1), Space: O(1)
# Topic/Category : Math
# Difficulty : Easy
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1,300):
            if i % 2 == 0 and i % n == 0:
                return i 
# Time = O(n), Space = O(1)
"""
n = 5
o/p = 10
"""
