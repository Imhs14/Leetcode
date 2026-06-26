class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
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
    
# Above solution having Time = O(m + n) , Space = O(1)

"""
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
