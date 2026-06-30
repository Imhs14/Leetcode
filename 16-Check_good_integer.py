# Question : 3248. Check Good Integer
# Complexity : Time: O(D), Space: O(D)
# Topic/Category : Math
# Difficulty : Easy

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

'''
n =
1234

Output
True
'''