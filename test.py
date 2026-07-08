class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        
        start = [(0,0),(0,3),(0,6),
                 (3,0),(3,3),(3,6),
                 (6,0),(6,3),(6,6)]
        
        for i,j in start:
            s = set()
            for row in range(i,i+3):
                for col in range(j, j+3):
                    item = board[i][j]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0 
        for num in s:
            if num - 1 not in s:
                nxt = num + 1
                length  = 1
                while nxt in s:
                    nxt += 1
                    length += 1
            result = max(longest, length)
        return result
    

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord[c] - ord['a']] += 1
            key = tuple(count)
            ang[key].append(c)
        return list(ang.values())
