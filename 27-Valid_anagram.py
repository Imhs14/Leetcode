# Question : 242. Valid Anagram
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sh = {}
        th = {}
        for char in s:
            if char not in sh:
                sh[char] = 1
            elif char in sh:
                sh[char] += 1
        
        for char in t:
            if char not in th:
                th[char] = 1
            elif char in th:
                th[char] += 1
        return sh == th
# Time = O(n), Space = O(1) as keys could be long as 26 keys not more than that!
# different ways to solve it is 
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sD = Counter(s)
        Td = Counter(t)
        return  sD == Td
# Time  = O(n), Space = O(n) 
'''s =
"anagram"
t =
"nagaram"
Output
True
'''"""
s = "anagram"
t = "nagaram"
o/p = True
"""
"""
s = "anagram"
t = "nagaram"
o/p = True
"""
