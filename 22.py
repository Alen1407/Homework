import random
def func_a(matrix, ls = []):
    if not ls:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    ls.append((i,j))
                    
    spot = random.choice(ls)
    print(spot)
    matrix[spot[0]][spot[1]] = 2
    ls.remove(spot)
    
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
        
        
def func_b(matrix):
    if (matrix[0][0] == matrix[0][1] == matrix[0][2] != 0) \
        or (matrix[1][0] == matrix[1][1] == matrix[1][2] != 0) \
        or (matrix[2][0] == matrix[2][1] == matrix[2][2] != 0) \
        or (matrix[0][0] == matrix[1][0] == matrix[2][0] != 0) \
        or (matrix[0][1] == matrix[1][1] == matrix[2][1] != 0) \
        or (matrix[0][2] == matrix[1][2] == matrix[2][2] != 0) \
        or (matrix[0][0] == matrix[1][1] == matrix[2][2] != 0) \
        or (matrix[0][2] == matrix[1][1] == matrix[2][0] != 0):
            return True
        return False
            
func_a(board)
print(board)
func_a(board)
print(board)
