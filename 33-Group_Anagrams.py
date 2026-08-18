# Question : 49. Group Anagrams
# Complexity : Time: O(N * M), Space: O(N)
# Topic/Category : Arrays & Hashing
# Difficulty : Medium
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        
        for s in strs: 
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)
            anagrams_dict[key].append(s)
            
        return list(anagrams_dict.values())
# Time O(n * m), space = O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s,t):
            if len(s) != len(t):
                return False
            letter_freq = {}
            for char in s:
                letter_freq[char] = letter_freq.get(char,0) +1
            for char in t:
                if char not in letter_freq:
                    return False
                letter_freq[char] -=1
                if letter_freq[char] <0:
                    return False
            return True
        result = []
        anagrams = strs
        j = len(anagrams)-1
        while j>=0:
            anagram = []
            anagram.append(anagrams[j])
            for i in range(j-1,-1,-1):
                if isAnagram(anagrams[j],anagrams[i]):
                    anagram.append(anagrams[i])
                    anagrams.pop(i)
                    j-=1
            
            result.append(anagram)
            j-=1
        return result
    
class Solution:
    def check_ana(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        H = {}
        for char in s:
            H[char] = H.get(char, 0) + 1
        for char in t:
            if (char not in H or H[char] == 0):
                return False
            H[char] -= 1
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = [0] * len(strs)
        ans = []
        for i, char in enumerate(strs):
            if (grouped[i] == 0):
                ls = [char]
                for j in range(i + 1, len(strs)):
                    if self.check_ana(strs[j], char):
                        ls.append(strs[j])
                        grouped[j] = 1    
                ans.append(ls)        
        return ans
"""
strs = ["eat","tea","tan","ate","nat","bat"]
o/p = [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
