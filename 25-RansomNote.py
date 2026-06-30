# Question : 383. Ransom Note
# Complexity : Time: O(M + N), Space: O(N)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
            
        for c in ransomNote:

            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1

        return True 

"""
Alternate ways of solving it
case : 1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        for letter in ransomNote:
            if letters.get(letter, 0) < 1:
                return False
            letters[letter] -= 1
        return True

case : 2
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True

case : 3
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine) # TC for Counter is O(n)
 
        for ch in ransomNote:
            if hashmap[ch] > 0:
                hashmap[ch]-=1
            else:
                return False
        return True
""" 

'''
ransomNote =
"a"

magazine =
"b"

Output
False
'''
