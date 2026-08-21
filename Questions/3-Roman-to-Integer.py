# Question : 13. Roman to Integer
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Math
# Difficulty : Easy
class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M':1000}
        n = 0
        prev = 0
        for x in s[::-1]:
            cur = val[x]
            if cur < prev :
                n -= cur        # prev isn't updated in that branch because it doesn't need to be — you're iterating right to left, so prev should always hold the largest value seen so far from the right.Think about why: when cur < prev, that means the current numeral is smaller than something to its right, so it's being subtracted (like the I in IV). But cur itself doesn't become the new "largest seen" — it's smaller than prev, so prev should stay exactly what it was.
            else:
                n += cur 
                prev = cur 
        return n 
if __name__ == '__main__':
    s = input("")
    obj = Solution()
    print(obj.romanToInt(s))
# eg MCMXCIV
'''
     Symbol	curr	prev	curr < prev?	Action	Running Total
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
'''s =
"MCMXCIV"
Output
1994
'''
"""
s = "III"
o/p = 3
"""
