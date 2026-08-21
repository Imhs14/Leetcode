# Question : 118. Pascal's Triangle
# Complexity : Time: O(N^2), Space: O(N^2)
# Topic/Category : Arrays & Math
# Difficulty : Easy

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        res = [[1]]
        re1 = []
        i,j = 1,0
        
        while i < numRows:
            if j == 0:
                re1.append(1)
                j += 1
            elif j < i:
                while j < i:
                    a = res[i-1][j] + res[i-1][j-1]
                    re1.append(a)
                    j+= 1
                
            if j == i:
                re1.append(1)
                res.append(re1)
                j = 0
                re1 = []
                i += 1
            
        return res

p1 = Solution()
print(p1.generate(5))

"""
numRows = 5
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""