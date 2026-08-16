# Build the matrix by reading line by line until End Of File (EOF)
matrix = []
while True:
    try:
        line = input().strip()
        if line:
            matrix.append([int(x) for x in line.split()])
    except EOFError:
        break

if matrix:
    n = len(matrix)
    
    # Step 1: Reverse each row in-place
    for i in range(n):
        matrix[i] = matrix[i][::-1]
        
    # Step 2: Transpose the matrix in-place
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements across the main diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Print the rotated matrix
    for row in matrix:
        print(*row)