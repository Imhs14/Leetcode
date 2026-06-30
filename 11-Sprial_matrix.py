# Question : 54. Spiral Matrix
# Complexity : Time: O(M * N), Space: O(1)
# Topic/Category : Matrices
# Difficulty : Medium

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        
        i, j = 0, 0 
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        total_elements = len(matrix) * len(matrix[0])
        while len(result) < total_elements:
            # 1. Move Right along the top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1  # Shrink top boundary
            
            # 2. Move Down along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Shrink right boundary
            
            # Check if there's still a valid row to traverse
            if top <= bottom:
                # 3. Move Left along the bottom row
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1  # Shrink bottom boundary
                
            # Check if there's still a valid column to traverse
            if left <= right:
                # 4. Move Up along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Shrink left boundary
        return result
    

''' 
Another way of solving it 

	class Solution:

	    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

	        m, n = len(matrix), len(matrix[0])

	        ans = []

	        i, j = 0, 0

	        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

	        direction = RIGHT

	 

	        UP_WALL = 0

	        RIGHT_WALL = n

	        DOWN_WALL = m

	        LEFT_WALL = -1

	 

	        while len(ans) != m*n:

	            if direction == RIGHT:

	                while j < RIGHT_WALL:

	                    ans.append(matrix[i][j])

	                    j += 1

	                i, j = i+1, j-1

	                RIGHT_WALL -= 1

	                direction = DOWN

	            elif direction == DOWN:

	                while i < DOWN_WALL:

	                    ans.append(matrix[i][j])

	                    i += 1

	                i, j = i-1, j-1

	                DOWN_WALL -= 1

	                direction = LEFT

	            elif direction == LEFT:

	                while j > LEFT_WALL:

	                    ans.append(matrix[i][j])

	                    j -= 1

	                i, j = i-1, j+1

	                LEFT_WALL += 1

	                direction = UP

	            else:

	                while i > UP_WALL:

	                    ans.append(matrix[i][j])

	                    i -= 1

	                i, j = i+1, j+1

	                UP_WALL += 1

	                direction = RIGHT

	        

	        return ans 

	        # Time: O(m*n) 

	        # Space: O(1)

	 '''