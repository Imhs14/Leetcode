# LeetCode Problem N/A: Check Good Integer
# URL: https://leetcode.com/problems/check-good-integer/description/
# Difficulty: Easy
# Category: Math
# Time Complexity: O(D)
# Space Complexity: O(D)

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        dig_sum, sq_sum = 0, 0
        for i in str(n):
            a = n %10
            p = n // 10
            n = p
            dig_sum += a
            sq_sum += a*a
        
        return  sq_sum - dig_sum >= 50 