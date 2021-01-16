matrix = [[1,2,3],[4,5,6],[7,8,9]]
tran_matrix=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        tran_matrix[j][i] = matrix[i][j]
for r in tran_matrix:
    print(r)
# print(tran_matrix)