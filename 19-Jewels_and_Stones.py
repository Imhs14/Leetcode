# Question : 771. Jewels and Stones
# Complexity : Time: O(M + N), Space: O(M)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        dic1 = {}
        for i,char in enumerate(jewels):
            dic1[char] = i
        for j in range(0, len(stones)):
            if stones[j] in dic1.keys():
                count += 1
        return count
    
# Above solution having Time = O(m + n) , Space = O(1)
"""
# Time = O(m + n), space = O(1)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        
        return count 
# this is better and the solution uses the hash sets

# Time = O(JxS) Space = O(1)
count = 0
for i in range(0,len(jewels)):
    j = 0
    while j < len(stones):
        if jewels[i] == stones[j]:
            count += 1
            j += 1
        else:
            j += 1
 return count
    """
'''jewels =
"aA"
stones =
"aAAbbbb"
Output
3
'''
"""
jewels = "aA"
stones = "aAAbbbb"
o/p = 3
"""
