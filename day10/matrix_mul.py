matrix_1 = [[1,2],[3,4]]
matrix_2 = [[1,2],[3,4]]
mul = [[0,0],[0,0]]

# mul = [[0 for x in range(3)] for y in range(3)]  
  
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            mul[i][j]+=matrix_1[i][k]*matrix_2[k][j]
           
print(mul)
      















    # mul[0][0]=matrix_1[0][0]*matrix_2[0][0]+matrix_1[0][1]*matrix_2[1][0]
    # mul[0][1]=matrix_1[0][0]*matrix_2[0][1]+matrix_1[0][1]*matrix_2[1][1]
    # mul[1][0]=matrix_1[1][0]*matrix_2[0][0]+matrix_1[1][1]*matrix_2[1][0]
    # mul[1][1]=matrix_1[1][0]*matrix_2[1][0]+matrix_1[1][1]*matrix_2[1][0]