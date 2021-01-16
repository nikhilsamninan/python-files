matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix_2 = [[1,2,3],[4,5,6],[7,8,9]]
sum = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        sum[i][j] = matrix_1[i][j] + matrix_2[i][j]
print(sum)
