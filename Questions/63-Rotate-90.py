matrix = [[0, 1, 2],[3, 4, 5],[6, 7, 8]] 
n = len(matrix)
print(matrix)
for i in range(n):
    for j in range(i+1,len(matrix)):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
print(matrix)

for i in range(n//2):
    for j in range(n):
        matrix[i][j],matrix[n - i - 1][j] = matrix[n - i - 1][j],matrix[i][j]
print(matrix)
