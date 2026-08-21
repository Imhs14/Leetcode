# Question : 48. Rotate Image
# Complexity : Time: O(N^2), Space: O(1)
# Topic/Category : Matrices
# Difficulty : Medium
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.
        n = len(matrix)
        # Transpose 
        for i in range(n):
            for j in range(i + 1 , n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reflection 
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][j - n - 1] = matrix[i][j - n - 1], matrix[i][j]
if __name__ == '__main__':
    # 1. Ask for the number of rows
    rows = int(input("Enter the number of rows: "))
    matrix = []
    print("Enter the entries row by row (separated by spaces):")
    for i in range(rows):
        # 2. Read the line, split it by spaces, and convert each part to an integer
        row = list(map(int, input().split()))
    
        # 3. Add the row to our main matrix
        matrix.append(row)
        print("Your matrix is:", matrix)
'''matrix =
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
'''
"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]
o/p = [[7,4,1],[8,5,2],[9,6,3]]
"""
