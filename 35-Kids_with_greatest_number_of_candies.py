class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for can in candies: 
            if (can + extraCandies) >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
# Time = O(n), Space = O(n)
"""
candies = [2,3,5,1,3]
extraCandies = 3
o/p = [True,True,True,False,True]
"""
