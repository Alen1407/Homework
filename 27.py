def check_row(ls):
    dic = {}
    for i in ls:
        if not str(i) in dic.keys():
            dic[str(i)] = 1
        else:
            return False
    return True
    
def sudoku_win(matrix):
    for row in matrix:
        if not check_row(row):
            return False
            
    for i in range(9):
        if not check_row([row[i] for row in matrix]):
            return False
    ls = []
    i = 3
    j = 3
    for k in range(9):
        for x in range(i-3,i):
            for y in range(j-3,j):
                ls.append(matrix[x][y])
        if not check_row(ls):
            return False
        ls = []
        
        i += 3
        
        if i > 9: i = 3; j += 3
              
    return True
    

matrix = [[1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9]]
          
print(sudoku_win(matrix))
