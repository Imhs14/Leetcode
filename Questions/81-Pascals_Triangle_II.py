class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rowIndex += 1   # Here we have the same problem as the pascal's Triangle I but the constraints were 1 <= numrows <= 30 and here in this Pascal's Triangle II 0 <= rowindex <= 33 
        # here in Pascal's Triangle 2 we will return the last row's list of elements.
        if rowIndex == 1: return [1]
        res = [[1]]
        re1 = []
        i,j = 1,0
        
        while i <= rowIndex:
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
            
        return res[rowIndex]

s = Solution()
print(s.getRow(4))
print(s.getRow(2))
print(s.getRow(1))
print(s.getRow(3))