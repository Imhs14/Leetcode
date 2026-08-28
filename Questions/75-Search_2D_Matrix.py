# Method 1 ,case 1
"""class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0,0
        while i < len(matrix):
            if matrix[i][j] == target:
                return True
            j+= 1
            if j == len(matrix[0]):
                j = 0
                i+= 1
        return False

p1 = Solution()

print(p1.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

# Time = O(n^2), Space = O(1)
p1 = Solution()
print(p1.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
"""
# Method 2, case 2 (playing with indexes)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j = len(matrix[0]) - 1
        p,q = 0,0
        for i in range(len(matrix)):
            if target <= matrix[i][j]:
                p,q = i,0
                break
          
        for q in range(len(matrix[0])):
            if matrix[p][q] == target:
                return True

        return False
# Time = O(m + n), Space = O(1)
p1 = Solution()

print(p1.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],20))