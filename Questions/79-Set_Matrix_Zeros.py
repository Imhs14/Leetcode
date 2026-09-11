# Question : 73. Set Matrix Zeroes
# Complexity : Time = O(M x N)^2, Space = O(1)
# Topic/Category : Array, Matrix, Hash Table
# Difficulty : Medium
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = float('inf')
                    if j != 0:
                        matrix[0][j] = float('inf')
                    else:
                        col = float('inf')
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n-1,0,-1):
            for j in range(m-1,0,-1):
                if matrix[i][0] == float('inf') or matrix[0][j] == float('inf'):
                    matrix[i][j] = 0
        
        for k in range(m-1,0,-1):       # this is the row operation for the edge case for the top right to 2nd element from left 
            if matrix[0][k] == float('inf') or matrix[0][0] == float('inf'):
                matrix[0][k] = 0
        
        for p in range(n):
            if matrix[p][0] == float('inf') or col == float('inf'):
                matrix[p][0] = 0
        return matrix
    
    # Time = O(M x N)^2, Space = O(1)

p = Solution()

print(p.setZeroes([[1,1,1],[1,0,1],[1,1,1]])) # [[1,0,1],[0,0,0],[1,0,1]]
print(p.setZeroes( [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))    # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(p.setZeroes([[1,2,3,4],[5,6,0,8],[9,10,11,12]]))  #[[1,2,0,4],[0,0,0,0],[9,10,0,]]
print(p.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

# Brute Force
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r,c = 0,0
                    while r < len(matrix[0]):
                        if matrix[i][r] != 0:
                            matrix[i][r] = float('inf')
                        r += 1
                    #print(matrix,'after 1st row changes')

                    while c < len(matrix):
                        if matrix[c][j] != 0:
                            matrix[c][j] = float('inf')
                        c += 1

                    #print(matrix,' after 2 col changes')
                    

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0

        return matrix
        
p = Solution()

print(p.setZeroes([[1,1,1],[1,0,1],[1,1,1]])) # [[1,0,1],[0,0,0],[1,0,1]]
print(p.setZeroes( [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))    # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(p.setZeroes([[1,2,3,4],[5,6,0,8],[9,10,11,12]]))  #[[1,2,0,4],[0,0,0,0],[9,10,0,]]
print(p.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))  # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Better solution Space = O(M)+O(N) , Time = (M x N)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = [0] * len(matrix[0])
        col = [0] * len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[j] = 1
                    col[i] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[j] == 1:
                    matrix[i][j] = 0
                elif col[i] == 1:
                    matrix[i][j] = 0

        return matrix

p = Solution()

print(p.setZeroes([[1,1,1],[1,0,1],[1,1,1]])) # [[1,0,1],[0,0,0],[1,0,1]]
print(p.setZeroes( [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))    # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(p.setZeroes([[1,2,3,4],[5,6,0,8],[9,10,11,12]]))  #[[1,2,0,4],[0,0,0,0],[9,10,0,]]
print(p.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))