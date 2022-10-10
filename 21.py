import math

def rotate_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(int(len(matrix)/2)):
            matrix[i][j], matrix[-i-1][-j-1] = matrix[-i-1][-j-1], matrix[i][j]


    return matrix

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

rows = 4;
columns = 4

'''for i in range(int(rows/2)):
    for j in range(columns):
        matrix[i][j], matrix[-i-1][-j-1] = matrix[-i-1][-j-1], matrix[i][j]
'''
matrix = rotate_matrix(matrix)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], sep=" ", end='')
    print()
