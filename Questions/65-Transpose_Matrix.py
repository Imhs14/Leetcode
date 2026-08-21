# Question : 867. Transpose Matrix
# Complexity : Time: O(R x C), Space: O(R x C)
# Topic/Category : Array, Matrix
# Difficulty : Easy
class Solution:
    def TransposeMatrix(self,matrix):
        fin = []
        n = len(matrix)
        for j in range(len(matrix[0])):
            res = []
            for i in range(n):
                res.append(matrix[i][j])
            fin.append(res)
        return fin
            
p1 = Solution()
print(p1.TransposeMatrix([[1,2,3],[4,5,6],[7,8,9]]))
