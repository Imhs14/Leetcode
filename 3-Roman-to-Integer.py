# LeetCode Problem 13: Roman to Integer
# URL: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy
# Category: Math
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M':1000}
        n = 0
        prev = 0
        for x in s[::-1]:
            cur = val[x]
            if cur < prev :
                n -= cur
            else:
                n += cur 
                prev = cur 
        return n 

if __name__ == '__main__':
    s = input("")
    obj = Solution()
    print(obj.romanToInt(s))

# eg MCMXCIV
''' Symbol	curr	prev	curr < prev?	Action	Running Total
      V	     5	     0   	     No	         +5	        5   
      I	     1	     5	         Yes	     -1         4
      C	     100	 1	          No	     +100	    104
      X	     10	     100          Yes	     -10	    94
      M	     1000	 10	          No	     +1000	    1094
      C	     100	1000	      Yes	      -100	     994
      M	     1000	100	           No	      +1000	     1994 
'''
"""
eg i/p & o/p :
"III"
3 
"""